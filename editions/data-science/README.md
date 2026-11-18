# Talent Stack: Data Science Edition

Students hire a data science team for real-world projects such as wildfire alerts, outbreak tracking and esports leagues. They learn what data careers do, what they pay, and what schooling they need.

- **Players:** 2–3 teams per deck
- **Time:** about 20 minutes
- **Grades:** 6–8
- **Series:** [Talent Stack](../../README.md), part of [Computer Science Offline](https://csoffline.org)
- **Status:** prototype. Core rules have been playtested; the Market Event, Secret Company and quest 4–12 cards have not yet.

## Contents

| File | What it is |
|---|---|
| [`cards.html`](cards.html) | All 44 cards with fronts and backs, plus 16 print-ready Letter sheets |
| [`rules-sheet.html`](rules-sheet.html) | One-page Letter how-to-play sheet |
| [`docs/scoring-and-balance.md`](docs/scoring-and-balance.md) | Scoring rules, trade rules, card lists, and balance-test results |
| [`docs/original-design-document.pdf`](docs/original-design-document.pdf) | The first design document, written under the earlier name "Data Science Deck: Career Launch" |
| [`tools/balance_check.py`](tools/balance_check.py) | Script that tests every quest against every Market and Company card |

## The deck

| Cards | Count | Notes |
|---|---|---|
| Career | 12 | Data Analyst, Machine Learning Engineer, Data Engineer, Chief Data Officer, AI Research Scientist, Cybersecurity Data Analyst, Bioinformatics Specialist, Sports Analytics Specialist, Game Data Analyst, Climate Data Scientist, Social Media Data Analyst, Healthcare Data Scientist |
| Project Quest | 12 | Every career is required by exactly 3 quests. Card backs show the scoring guide. |
| Market Event | 12 | Draw 1 face-up per game. |
| Secret Company | 8 | Each team draws 1 in secret. |

Tech stack icons: **SQL, Python, Tableau, Cloud, Security**.

## Printing

Open `cards.html` or `rules-sheet.html` in Chrome. Print on Letter paper at 100% scale, with margins set to None and background graphics on. For the cards, print two-sided and flip on the long edge. The cards file prints 16 pages, alternating fronts and their matching backs.

## Balance check

```bash
python tools/balance_check.py
```

The script needs Python 3 and no other packages. It scores all 220 possible teams for every quest, Market and Company combination. It confirms that completing the quest is always the best or tied-best plan, and counts how many different backup strategies each quest has. Update the tables at the top of the script whenever card values change.

## Before final printing

- **Salaries are placeholders** from the original design document. Each card back says "salary unverified." Cite a source and date, such as the BLS Occupational Outlook Handbook, before printing final cards.
- **Playtest the replay decks and quests 4–12.** In the simulation, quests 8 and 9 tie most often, about 1 game in 10.
- **Educational standards:** map the game to specific grade 6–8 standards and add 2–3 learning objectives.
