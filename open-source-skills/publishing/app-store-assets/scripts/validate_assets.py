#!/usr/bin/env python3
"""Validate App Store assets against Apple's published specs (see ../references/specs.md).

Usage:
  validate_assets.py PATH [PATH ...] [--kind auto|icon|screenshot|preview|header|search|iae-card|iae-details]

PATH may be a file or a directory (searched recursively). Needs ffprobe (stdlib only otherwise).
Exit code 1 if any FAIL. Content rules (no prices, 4+, etc.) need the manual checklist.
Spec tables fetched from developer.apple.com on 2026-10-20; re-verify before final export.
"""
import argparse, json, os, subprocess, sys
from collections import defaultdict

IMG_EXT = {".png", ".jpg", ".jpeg"}
VID_EXT = {".mov", ".m4v", ".mp4"}

def both(sizes):
    out = set()
    for w, h in sizes:
        out.add((w, h)); out.add((h, w))
    return out

# ---- screenshot tables: name -> (portrait sizes, required?) ----
SHOT = {
    "iPhone Duo outer": ([(1398, 2034)], False),
    "iPhone Duo inner": ([(2007, 2853)], False),
    "iPhone 6.9in (Dynamic Island large)": ([(1260, 2736), (1290, 2796), (1320, 2868)], False),
    "iPhone 6.5in (Face ID large)": ([(1284, 2778), (1242, 2688)], False),
    "iPhone 6.1/6.3in (Dynamic Island medium)": ([(1179, 2556), (1206, 2622)], True),
    "iPhone Face ID medium": ([(1170, 2532), (1125, 2436), (1080, 2340)], False),
    "iPhone Home Button large": ([(1242, 2208)], False),
    "iPhone Home Button medium": ([(750, 1334)], False),
    "iPhone 4in": ([(640, 1096), (640, 1136)], False),
    "iPhone 3.5in": ([(640, 920), (640, 960)], False),
    "iPad 13in": ([(2064, 2752), (2048, 2732)], True),
    "iPad 11in": ([(1488, 2266), (1668, 2420), (1668, 2388), (1640, 2360)], False),
    "iPad 10.5in": ([(1668, 2224)], False),
    "iPad 9.7in": ([(1536, 2008), (1536, 2048), (768, 1004), (768, 1024)], False),
    "Mac": ([(1280, 800), (1440, 900), (2560, 1600), (2880, 1800)], False),
    "Apple TV": ([(1920, 1080), (3840, 2160)], False),
    "Vision Pro": ([(3840, 2160)], False),
    "Watch Ultra 3/4": ([(422, 514)], False),
    "Watch Ultra/Ultra 2": ([(410, 502)], False),
    "Watch S10-12": ([(416, 496)], False),
    "Watch S7-9": ([(396, 484)], False),
    "Watch S4-6/SE": ([(368, 448)], False),
    "Watch S1-3": ([(312, 390)], False),
}
# Mac/TV/Vision are landscape-only 16:10 / 16:9: portrait swap would wrongly match; handle below.
LANDSCAPE_ONLY = {"Mac", "Apple TV", "Vision Pro"}
FIXED_ORIENT = {n for n in SHOT if n.startswith("Watch")}  # watch is portrait as listed

# ---- preview tables ----
PREV = {
    "iPhone (886x1920 class)": [(886, 1920)],
    "iPhone/iPad? 1080x1920 class": [(1080, 1920)],
    "iPhone 4.7in": [(750, 1334)],
    "iPad (1200x1600)": [(1200, 1600)],
    "iPad (900x1200)": [(900, 1200)],
    "Mac/Apple TV": [(1920, 1080)],
    "Vision Pro": [(3840, 2160)],
}
PREV_LANDSCAPE_ONLY = {"Mac/Apple TV", "Vision Pro"}

# ---- creative assets ----
def in_range(w, h, lo, hi):
    return lo[0] <= w <= hi[0] and lo[1] <= h <= hi[1]

def probe(path):
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", path],
            capture_output=True, text=True, timeout=60)
        return json.loads(r.stdout or "{}")
    except FileNotFoundError:
        sys.exit("ffprobe not found (brew install ffmpeg)")
    except Exception as e:
        return {"error": str(e)}

def has_alpha(stream):
    pf = (stream.get("pix_fmt") or "").lower()
    return any(t in pf for t in ("rgba", "argb", "bgra", "abgr", "ya8", "ya16", "gbra", "yuva", "pal8"))

class Report:
    def __init__(self): self.rows = []; self.fail = 0
    def add(self, level, path, msg):
        self.rows.append((level, path, msg))
        if level == "FAIL": self.fail += 1
    def show(self):
        for lv, p, m in self.rows:
            print(f"[{lv}] {os.path.relpath(p)}: {m}")

def guess_kind(path, info):
    name = os.path.basename(path).lower()
    ext = os.path.splitext(path)[1].lower()
    if ext in VID_EXT: return "preview"
    for k, tag in (("icon", "icon"), ("header", "header"), ("search", "search"),
                   ("iae-card", "event-card"), ("iae-details", "event-detail")):
        if tag in name: return k
    return "screenshot"

def check_image_common(rep, path, st):
    ext = os.path.splitext(path)[1].lower()
    if ext not in IMG_EXT: rep.add("FAIL", path, f"format {ext} not accepted (use jpg/jpeg/png)")
    if has_alpha(st): rep.add("FAIL", path, f"has alpha channel (pix_fmt={st.get('pix_fmt')}); flatten onto opaque bg")

def match_shot(w, h):
    hits = []
    for name, (sizes, _) in SHOT.items():
        if name in LANDSCAPE_ONLY:
            ok = (w, h) in set(sizes)
        elif name in FIXED_ORIENT:
            ok = (w, h) in set(sizes)
        else:
            ok = (w, h) in both(sizes)
        if ok: hits.append(name)
    return hits

def validate_image(rep, path, kind, st, shots_by_class):
    w, h = st.get("width"), st.get("height")
    check_image_common(rep, path, st)
    if kind == "icon":
        if (w, h) != (1024, 1024): rep.add("FAIL", path, f"icon must be 1024x1024, got {w}x{h}")
        elif not path.lower().endswith(".png"): rep.add("WARN", path, "icon should be PNG")
        else: rep.add("OK", path, "icon 1024x1024, no alpha")
        return
    if kind == "screenshot":
        hits = match_shot(w, h)
        if not hits:
            rep.add("FAIL", path, f"{w}x{h} matches no accepted screenshot size (see references/specs.md)")
        else:
            rep.add("OK", path, f"{w}x{h} = {' | '.join(hits)}")
            shots_by_class[hits[0]].append(path)
        return
    if kind == "header":
        ok = (w, h) == (3840, 1646) or ((w, h) == (5244, 2950) and path.lower().endswith(".png"))
        rep.add("OK" if ok else "FAIL", path, f"header {w}x{h}" + ("" if ok else " must be 3840x1646 (21:9) or 5244x2950 PNG (16:9)"))
        return
    if kind == "search":
        ok = in_range(w, h, (1920, 1280), (3840, 2560)) and abs(w / h - 1.5) < 0.005 \
            or ((w, h) == (5244, 2950) and path.lower().endswith(".png"))
        rep.add("OK" if ok else "FAIL", path, f"search {w}x{h}" + ("" if ok else " must be 3:2 within 1920x1280-3840x2560 or 5244x2950 PNG"))
        return
    if kind == "iae-card":
        ok = in_range(w, h, (1920, 1080), (3840, 2160)) and abs(w / h - 16 / 9) < 0.005
        rep.add("OK" if ok else "FAIL", path, f"IAE card {w}x{h}" + ("" if ok else " must be 16:9 within 1920x1080-3840x2160"))
        return
    if kind == "iae-details":
        ok = in_range(w, h, (1080, 1920), (2160, 3840)) and abs(w / h - 9 / 16) < 0.005
        rep.add("OK" if ok else "FAIL", path, f"IAE details {w}x{h}" + ("" if ok else " must be 9:16 within 1080x1920-2160x3840"))
        return

def validate_video(rep, path, kind, data):
    ext = os.path.splitext(path)[1].lower()
    streams = data.get("streams", [])
    v = next((s for s in streams if s.get("codec_type") == "video"), None)
    a = [s for s in streams if s.get("codec_type") == "audio"]
    if not v:
        rep.add("FAIL", path, "no video stream"); return
    w, h = v["width"], v["height"]
    dur = float(data.get("format", {}).get("duration") or v.get("duration") or 0)
    size_mb = int(data.get("format", {}).get("size", 0)) / 1e6
    num, den = (v.get("avg_frame_rate") or "0/1").split("/")
    fps = float(num) / float(den) if float(den) else 0
    codec = v.get("codec_name")
    if kind == "preview":
        lo, hi = 15, 30
    elif kind in ("iae-card", "iae-details"):
        lo, hi = 15, 30
    else:
        lo, hi = 5, 30
    if not (lo <= dur <= hi + 0.05): rep.add("FAIL", path, f"duration {dur:.1f}s outside {lo}-{hi}s")
    if kind == "preview":
        if ext not in VID_EXT: rep.add("FAIL", path, f"extension {ext}")
        if codec == "prores":
            if ext != ".mov": rep.add("FAIL", path, "ProRes must be .mov")
        elif codec != "h264": rep.add("FAIL", path, f"codec {codec}; need H.264 or ProRes 422 HQ")
        if fps > 30.5: rep.add("FAIL", path, f"{fps:.1f} fps > 30 max for previews")
        if size_mb > 500: rep.add("FAIL", path, f"{size_mb:.0f} MB > 500 MB")
        if codec == "h264":
            br = int(data.get("format", {}).get("bit_rate", 0)) / 1e6
            if br > 14: rep.add("WARN", path, f"bit rate {br:.1f} Mbps; Apple target is 10-12")
            prof = v.get("profile", "")
            if prof and prof not in ("High", "Main", "Baseline", "Constrained Baseline"):
                rep.add("WARN", path, f"H.264 profile {prof}; up to High L4.0")
            if v.get("level") and int(v["level"]) > 40: rep.add("WARN", path, f"H.264 level {v['level']} > 4.0")
        if not a:
            rep.add("WARN", path, "no audio track (OK; previews autoplay muted, but ASC sometimes needs a silent stereo track)")
        else:
            s = a[0]
            if s.get("channels") != 2: rep.add("FAIL", path, f"audio channels {s.get('channels')}; need stereo")
            if s.get("sample_rate") not in ("44100", "48000"): rep.add("FAIL", path, f"audio {s.get('sample_rate')} Hz; need 44.1/48 kHz")
        ok = False
        for name, sizes in PREV.items():
            ss = set(sizes) if name in PREV_LANDSCAPE_ONLY else both(sizes)
            if (w, h) in ss: ok = True; rep.add("OK", path, f"{w}x{h} = {name}, {dur:.1f}s, {fps:.0f}fps, {codec}"); break
        if not ok: rep.add("FAIL", path, f"{w}x{h} not an accepted preview resolution (e.g. 886x1920, 1920x886, 1200x1600)")
        return
    # creative video
    if not (29 <= fps <= 31 or 59 <= fps <= 61):
        rep.add("FAIL", path, f"{fps:.1f} fps; need 30 or 60")
    if ext not in VID_EXT: rep.add("FAIL", path, f"extension {ext}")
    spec = {
        "header": lambda: (w, h) == (3840, 1646) or (w, h) == (5244, 2950),
        "search": lambda: in_range(w, h, (1920, 1280), (3840, 2560)) and abs(w / h - 1.5) < 0.005 or (w, h) == (5244, 2950),
        "iae-card": lambda: in_range(w, h, (1920, 1080), (3840, 2160)) and abs(w / h - 16 / 9) < 0.005,
        "iae-details": lambda: in_range(w, h, (1080, 1920), (2160, 3840)) and abs(w / h - 9 / 16) < 0.005,
    }.get(kind)
    if spec and not spec(): rep.add("FAIL", path, f"{w}x{h} not valid for {kind}")
    else: rep.add("OK", path, f"{kind} video {w}x{h}, {dur:.1f}s, {fps:.0f}fps")

def collect(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                for f in sorted(files):
                    if os.path.splitext(f)[1].lower() in IMG_EXT | VID_EXT: out.append(os.path.join(root, f))
        elif os.path.isfile(p): out.append(p)
        else: print(f"[WARN] {p}: not found")
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--kind", default="auto",
                    choices=["auto", "icon", "screenshot", "preview", "header", "search", "iae-card", "iae-details"])
    args = ap.parse_args()
    rep = Report()
    shots = defaultdict(list)
    files = collect(args.paths)
    if not files: sys.exit("no image/video files found")
    for f in files:
        data = probe(f)
        if not data.get("streams"):
            rep.add("FAIL", f, f"unreadable: {data.get('error', 'ffprobe found no streams')}"); continue
        ext = os.path.splitext(f)[1].lower()
        kind = args.kind if args.kind != "auto" else guess_kind(f, data)
        if ext in VID_EXT:
            validate_video(rep, f, kind if kind != "screenshot" else "preview", data)
        else:
            validate_image(rep, f, kind, data["streams"][0], shots)
    for cls, lst in shots.items():
        if len(lst) > 10: rep.add("FAIL", lst[0], f"{len(lst)} screenshots in class '{cls}'; max 10 per device size")
        elif len(lst) < 1: pass
    present = set(shots)
    if shots:
        iphone = [c for c in present if c.startswith("iPhone")]
        if iphone and not (present & {"iPhone 6.1/6.3in (Dynamic Island medium)", "iPhone 6.9in (Dynamic Island large)", "iPhone 6.5in (Face ID large)"}):
            rep.add("WARN", files[0], "no required iPhone Dynamic Island screenshot set found (6.1/6.3in required; larger class can fall back)")
        if not any(c.startswith("iPad") for c in present):
            rep.add("INFO", files[0], "no iPad 13in screenshots: required only if the app runs on iPad")
    rep.show()
    ok = sum(1 for r in rep.rows if r[0] == "OK")
    print(f"\n{len(files)} files | {ok} OK | {rep.fail} FAIL | "
          f"{sum(1 for r in rep.rows if r[0]=='WARN')} WARN")
    print("Reminder: run references/checklist.md for content rules (no prices/URLs, 4+, real UI, etc.)")
    sys.exit(1 if rep.fail else 0)

if __name__ == "__main__":
    main()
