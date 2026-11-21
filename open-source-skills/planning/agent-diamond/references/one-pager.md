# How to master graph engineering – the full course on one page

## 1. What a graph is
- A box is one job you would hand to one assistant.
- An arrow means the second job needs the first job’s result.
- Running notes travel with the work.

## 2. The fake edge
- An arrow where no work flows.
- For every “and then” ask: does the next job need the last job’s result?
- If no, the waiting is wasted. You will find two or three in any system you draw.

## 3. The diamond – the one pattern that pays
- Split the job, run workers side by side, check their work, merge into one answer.
- Measured at 80.2% better than a single agent on an internal research test (June 2025, older models, roughly 15× the usage of a chat).

## 4. The checker
- Never let the same agent grade its own homework.
- Top models caught no more than 21.1% of known real errors in their own kind of work.
- Separate checkers with different questions:
  - Is it correct?
  - Is it current?
  - Is the source real?

## 5. The stop rule
- 180 setups, same budget:
  - Work that splits → teams scored 80.9% higher
  - Step-by-step work → 39% to 70% percent WORSE
- A graph buys breadth, it does not buy better judgment.
- Ask first: where does my work split?

## 6. The human gate
- Put your approval where a mistake would be expensive to undo, not on every step.
- The send, the publish, the refund end at you: the last yes.
- Measure on what matters: money landed, customers stayed, tests ran.

## 7. The four safety rules
- Every loop gets a maximum number of rounds.
- One job writes to any one file.
- Routing lives in written steps, the AI fills the jobs.
- Always a cap on how many agents can spawn.

## 8. Three builds you can copy
- Graph 1 – deep research desk: 5 researchers + a skeptic replace a week of googling (prompt included).
- Graph 2 – SEO content machine: 3 researchers to outline → fact-checked draft, never publishes without you (prompt included).
- Graph 3 – go-to-market kit: research to positioning page → parallel assets to your approval (prompt included).

## 9. Quick legend
- Split / fan-out
- Job / task
- Check gate
- Running notes
- Your approval gate
- Data / storage
- Loop / repeat
- Agents / workers

## Build order
draw your system → delete the fake edges → wire one diamond → add the checker → place your gate → paste a build prompt
