<p align="center"><a href="https://csoffline.org"><img src="assets/cs-offline-logo.jpg" alt="Computer Science Offline" width="600"></a></p>

# Talent Stack

*Part of the **[Computer Science Offline](https://csoffline.org)** project: hands-on, screen-free activities that teach computer science. Visit [csoffline.org](https://csoffline.org) for more.*

**Talent Stack** is a series of classroom card games about tech careers for middle school students (grades 6–8). In every edition, teams act as hiring managers. They draft a three-person team from career cards, seeing only the job title, salary tier and tech skills, to complete a Project Quest on a budget. Then they flip the cards to audit the real salaries, degrees and job duties.

One game takes about 20 minutes, which fits a single class activity.

## Editions

| Edition | Folder | Status |
|---|---|---|
| **Data Science Edition** | [`editions/data-science`](editions/data-science) | Prototype, in playtesting |

## Repository layout

```
talent_stack_card_game/
├── README.md                  ← you are here
├── assets/                    ← Computer Science Offline logo
├── shared/                    ← used by every edition
│   ├── core-rules.md          ← the game engine every edition shares, and balance rules
│   └── icons/retro/           ← retro pixel icons for the Round 2 trade abilities
└── editions/
    └── data-science/          ← one folder per edition
        ├── README.md
        ├── cards.html         ← every card, printable
        ├── rules-sheet.html   ← one-page how-to-play sheet
        ├── docs/              ← design notes and balance results
        └── tools/             ← balance-check script
```

## Printing

Each edition has two printable pages:

- `cards.html`: every card at tarot size (2.75″ × 4.75″), laid out 6 per Letter sheet with crop marks. Backs are mirrored for two-sided printing.
- `rules-sheet.html`: a one-page Letter rules sheet.

Open the file in Chrome, then print on Letter paper at **100% scale**, with **margins set to None** and **background graphics on**. For the cards, print two-sided and **flip on the long edge**.

## Adding a new edition

1. Copy `editions/data-science` to `editions/<new-edition>`, for example `editions/cybersecurity`.
2. Replace the edition content: career cards, tech stack icons, quests, Market Event cards and Secret Company cards. [`shared/core-rules.md`](shared/core-rules.md) lists what each edition must define.
3. Update the tables in `tools/balance_check.py` and run it until every quest passes.
4. Add the edition to the table above.
