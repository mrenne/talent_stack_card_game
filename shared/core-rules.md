# Talent Stack core rules

Every Talent Stack edition uses the same game engine. An edition changes the **content**: which careers, skills and projects are in the deck. The **rules** stay the same. This file describes the shared engine, what each edition has to supply, and the balance rules that keep every edition fair.

## What every edition shares

| Part | How it works |
|---|---|
| **Teams** | 2–3 teams per deck, so at least 3 career cards stay in the pool for the Round 2 trade. At a table of 2–3 students, each student is a team. At a table of 4–6, students pair up. |
| **Blind draft** | Snake order (A → B → C → C → B → A …) until every team has 3 career cards. Teams choose from card fronts only. |
| **Audit** | Flip the cards and score: **+5** per required role, **+1** per stand-in (a card that shares a tech icon with a missing role), **+3** at or under the budget cap or **−1 per $10,000 over**, and **+1 / +3** tech synergy (most-shared icon on 2 or 3 cards). |
| **Round 2 trade** | Lowest Round 1 score goes first. Each team makes one trade with the pool. Retro icons on card backs give trade abilities: **Call Out** (rotary phone), **Save** (floppy disk), **Rewind** (VHS tape), **Preview** (CRT computer). The icons are in [`icons/retro`](icons/retro). |
| **Trade rulings** | Rewind only undoes a pool trade. A team that gets Called Out still makes its own trade. A card just taken by a Call Out can't be Called Out again that round. Abilities belong to the card. |
| **Team pitch** | 30 seconds, judged by the teacher and scored 0–3: a duty from every card, why the team fits the quest, finished on time. |
| **Final score** | Final audit + Secret Company bonus + pitch. Ties go to the **lower** total degree points (Bachelor's 1, Master's 2, Ph.D. 3). |
| **Replay decks** | One **Market Event** card is drawn face-up and changes the game for everyone. Each team draws one **Secret Company** card that pays a bonus at the end. |

## What each edition supplies

1. **Career cards (12 recommended):** title, salary tier ($ / $$ / $$$), two tech stack icons, domain, a two-sentence description, minimum degree, median salary with a cited source, and one retro trade icon. Give each trade icon to 3 cards, spread across tiers.
2. **Tech stack icons (about 5):** the skills that score synergy, for example SQL, Python, Tableau, Cloud and Security in the Data Science Edition.
3. **Project Quest cards (12 recommended):** a mission, 3 required roles and a budget cap. Every career should be required by the same number of quests, and no quest should need more than one $$$ role.
4. **Market Event cards (about 12):** effects on salaries, budget caps or scoring, each with a real-world reason.
5. **Secret Company cards (about 8):** bonus conditions worth at most +2.

## Balance rules

Check these with the edition's `tools/balance_check.py` before printing:

- **Completing the quest must always score best or tied-best**, under every Market and Company combination.
- **Budget caps** should be $3,000–$7,000 above the exact cost of the required lineup, so teams only find out whether they made budget during the audit.
- **Secret Company bonuses** never exceed +2.
- **A Market card that raises salaries for required roles** also needs a matching budget cap increase. Otherwise completing the quest stops being the best plan.
- **Per-card Market bonuses** are capped at +2 per team.
