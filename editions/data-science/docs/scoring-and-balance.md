# Revised Scoring: Talent Stack: Data Science Edition

*Formerly "Data Science Deck: Career Launch." The [original design document](original-design-document.pdf) still uses the old name. Re-run the balance results below with [`../tools/balance_check.py`](../tools/balance_check.py).*

Replaces Section 3, Phase 2 ("The Audit Flip & Score") and the Sample Project Quest budget caps in the GDD.

## Design goals

1. **Completing the quest is always the best plan.** Under the old rules, leaving out a required role beat filling all three in every sample quest.
2. **Losing a required role to another team isn't fatal.** There is only one copy of each card, so a team that misses a role can still finish close behind.
3. **The audit math matters.** Budgets are tight, so students have to add salaries carefully to know whether they made it.
4. **Every rule is easy to score.** No comparisons between teams, and no ambiguous degree values.

## Draft order

- Use a **snake draft** (A → B → C → C → B → A → A → B → C) so the first pick isn't a permanent advantage.
- Randomize first pick each round (roll a die, or give it to the lowest scorer from the previous round).
- **Teams per deck: 2 to 3** (settled). With 4 teams, all 12 cards would be drafted and the pool would be empty for the Round 2 trade. With 3 teams, 3 cards stay in the pool; with 2 teams, 6 do. At a table of 2–3 students, each student is a team. At a table of 4–6, students pair up.

## Audit scoring (max 19 points)

| Category | Points | Rule |
|---|---|---|
| **1. Role Match** | **+5** per required role | Each drafted card that matches a role on the Quest card. |
| **2. Stand-In** | **+1** per missing role | For each required role you don't have, one of your other cards can stand in if it shares a Tech Stack icon with that role. Each card can stand in for only one role. |
| **3. Budget Audit** | **+3** if at or under cap | If over the cap, **lose 1 point for every $10,000 over** (round up). Example: $17,000 over = −2. |
| **4. Tech Synergy** | **+1** or **+3** | Look at your *most-shared* icon only: on 2 cards = +1, on all 3 cards = +3. Pairs don't stack. |

**Tiebreaker:** add up each team's degree points using the *minimum* degree on each card (Bachelor's = 1, Master's = 2, Ph.D. = 3). The lower total wins, because that team built the strongest lineup with the least training. (Or flip it to "higher wins" if you'd rather reward expertise. Either way, it no longer adds points.)

> To make this work, the catalog's degree column should list one *minimum* degree per card instead of "Master's / Bachelor's" ranges.

## Round 2: Fast Trade (retro trade icons)

Every career card back has one retro tech icon. It's hidden during the blind draft and revealed at the audit flip, so Round 1 is pure guesswork and Round 2 is an informed decision.

**Base trade:** each team makes **one** trade: swap one of its cards for any face-up card in the unpicked pool (front side only, no peeking). The team with the lowest Round 1 score trades first.

| Icon | Ability | When it applies |
|---|---|---|
| Rotary phone | **Call Out**: instead of trading with the pool, trade this card for any card on another team (not a Save card). The other team can't refuse. | Your trade, using this card |
| Floppy disk | **Save**: this card is locked in. No other team can Call Out it. | Always (passive) |
| VHS tape | **Rewind**: if your re-audit score is lower than your Round 1 score, undo your pool trade. | After the re-audit |
| CRT computer | **Preview**: before you trade, peek at the backs of 2 pool cards. | Your trade |

**Trade rulings (settled):**

1. **Rewind only undoes a pool trade.** It can't undo a Call Out, whether your team made it or another team made it against you. That way one team's Rewind never changes another team's cards.
2. **A team that gets Called Out still makes its own trade.** If it hasn't had its turn yet, it trades normally when its turn comes.
3. **No Call-Out ping-pong.** A card that was just taken by a Call Out can't be Called Out again this round. *(Added so two Call Out teams can't trade the same card back and forth.)*
4. **Abilities belong to the card, not the team.** A card you trade away takes its icon with it. Because each team makes only one trade, a card you receive can't be used for another trade this round, though a Save card you receive still protects itself.

Each icon appears on 3 cards, and each tier has a mix, so cheap cards are as likely as expensive ones to carry a strong ability:

| Icon | $ | $$ | $$$ |
|---|---|---|---|
| Rotary phone | Social Media Data Analyst | Bioinformatics Specialist | AI Research Scientist |
| Floppy disk | Data Analyst | Cybersecurity Data Analyst | Chief Data Officer |
| VHS tape | Sports Analytics Specialist | Healthcare Data Scientist, Climate Data Scientist | — |
| CRT computer | Game Data Analyst | Data Engineer | Machine Learning Engineer |

Icons never add points, so the audit scoring above stays balanced. Data Engineer and ML Engineer, the two most-wanted roles, carry Preview rather than Save, so they can still be called away.

## Replay decks: Market Events and Secret Companies

Added after playtests showed little reason to play again. Once students had seen every card back, the blind draft wasn't blind anymore, and the best strategy was always the same.

**Setup additions:** draw 1 Market Event card face-up (it applies to every team for the whole game). Each team secretly draws 1 Company card and keeps it hidden until final scoring.

**Final score = final audit + Company bonus + pitch.** The Company bonus is added only at the end, so Round 1 scores, trade order and Rewind all use the audit score alone.

### Market Event cards (12)

| Card | Effect |
|---|---|
| Steady Market | No changes. |
| AI Boom | Python roles cost +$10,000. Every budget cap rises +$20,000. |
| Cloud Sale | Cloud roles cost −$10,000. |
| Cyberattack! | +1 point per Security card (max +2). |
| Dashboard Craze | +1 point per Tableau card (max +2). |
| Internship Program | $ roles cost −$10,000. |
| Talent Shortage | $$$ roles cost +$15,000. Every budget cap rises +$15,000. |
| Investor Bonus | Every budget cap rises +$30,000. |
| Hiring Freeze | Each team may draft at most one $$$ role. |
| Open Source Week | Tech synergy +1 more (+2 pair, +4 all three). |
| Audit Season | Over budget costs −2 per $10,000 (instead of −1). |
| Grad Rush | Bachelor's-degree roles cost −$5,000. |

### Secret Company cards (8)

| Card | Bonus at final scoring |
|---|---|
| Startup | +2 if total payroll is $300,000 or less (after Market changes) |
| Big Tech | +2 if the team includes a $$$ role |
| Nonprofit | +1 per $ role (max +2) |
| Research Lab | +2 if degree points total 5 or more |
| Security Firm | +2 if the team has a Security card |
| Creative Studio | +2 if the team has a Tableau card |
| Cloud Company | +2 if 2 or more cards have Cloud |
| Mid-Size Agency | +2 for one $, one $$ and one $$$ role |

### Balance check

All 324 combinations (3 quests × 12 markets × 9 company options, counting no company) were scored over all 220 possible teams.

- **The full required lineup is never beaten.** It ties the best other team in 9 of 324 cases.
- **Strategy now changes from game to game.** Without these decks, each quest had one best backup plan for a team that couldn't get all three roles. Now there are 14–21 different best backup plans per quest.
- **Two cards were retuned during testing.** AI Boom first only raised Python salaries, which pushed every full lineup over budget, so it now also raises caps by $20,000. Open Source Week first doubled synergy, which let off-quest teams win, so it now adds +1 instead.
- **Rule for new cards:** keep any Company bonus at +2 or less, and pair any market that raises required-role salaries with a matching cap increase.

## Pitch scoring (max 3 points, replaces the class vote)

**The teacher is the judge.** The teacher awards 1 point for each:

- [ ] Named a real job duty from the back of **every** card.
- [ ] Explained **why** this team fits the quest (not just listed roles).
- [ ] Finished within 30 seconds.

## Revised quest budget caps

| Quest | Required roles | Required total | Old cap | **New cap** |
|---|---|---|---|---|
| 1 Autonomous School Transit | Data Engineer, ML Engineer, Cyber Data Analyst | $367,000 | $350,000 | **$370,000** |
| 2 Video Game Economy Engine | Game Data Analyst, Data Engineer, ML Engineer | $357,000 | $330,000 | **$360,000** |
| 3 Global Climate Prediction | Climate Data Scientist, Data Engineer, Bioinformatics Specialist | $345,000 | $340,000 | **$350,000** |

Each cap is only $3,000–$5,000 above the exact lineup, so students can't confirm they made it from the tier badges alone. They'll find out during the audit flip.

### Quests 4–12 (added so every role is needed)

The original 3 quests never required 6 of the 12 roles, and every quest needed Data Engineer. With these 9 added, **every role is required by exactly 3 of the 12 quests**, and no quest needs more than one $$$ role, so Hiring Freeze never makes a quest impossible.

| Quest | Required roles | Required total | Cap |
|---|---|---|---|
| 4 Pro League Draft Predictor | Sports Analytics, AI Research Scientist, Data Analyst | $320,000 | **$325,000** |
| 5 Hospital Early-Warning System | Healthcare Data Scientist, Cybersecurity Data Analyst, AI Research Scientist | $370,000 | **$375,000** |
| 6 Viral Video Trend Tracker | Social Media Data Analyst, Data Analyst, ML Engineer | $300,000 | **$305,000** |
| 7 School District Data Makeover | Chief Data Officer, Data Analyst, Cybersecurity Data Analyst | $374,000 | **$380,000** |
| 8 Outbreak Tracker | Healthcare Data Scientist, Bioinformatics, Social Media Data Analyst | $304,000 | **$310,000** |
| 9 Esports League Launch | Game Data Analyst, Sports Analytics, Chief Data Officer | $370,000 | **$375,000** |
| 10 Wildfire Alert App | Climate Data Scientist, Social Media Data Analyst, AI Research Scientist | $340,000 | **$345,000** |
| 11 Global Food Forecast | Climate Data Scientist, Bioinformatics, Chief Data Officer | $410,000 | **$415,000** |
| 12 Youth Fitness Game App | Game Data Analyst, Sports Analytics, Healthcare Data Scientist | $298,000 | **$305,000** |

Each cap is the lineup total plus at least $3,000, rounded up to the next $5,000, so every cap is $3,000–$7,000 above the exact lineup.

**Balance check (all 12 quests × 12 markets × 9 company options, counting no company):** the full required lineup is never beaten. With no market or company card, it wins by 2–4 points. Each quest has 8–25 different best backup plans, depending on the market and companies drawn. Quests 8 and 9 tie most often, in 10 and 12 of 108 combinations. That's still fine, but watch those two in playtests.

**Quest card tip:** print tier ranges on each Quest card ($ ≈ $78–92k, $$ ≈ $102–125k, $$$ ≈ $140–190k) so students can estimate during the draft.

## Simulation check

All 220 possible 3-card teams were scored under these rules for each quest:

| Quest | Full required lineup | Best team missing one role | Best team with only one required role |
|---|---|---|---|
| 1 Transit | **19** (unique top score) | 15–17 | ≤ 13 |
| 2 Game | **19** (unique top score) | 15–17 | ≤ 13 |
| 3 Climate | **19** (unique top score) | 15–16 | ≤ 13 |

Under the old rules, the full lineup scored 6, while skipping a role scored 9–11.

## Still worth fixing (outside scoring)

- **Salaries** are still unsourced placeholders from the design doc. Cite a source and date (for example the BLS Occupational Outlook Handbook) before printing final cards.
