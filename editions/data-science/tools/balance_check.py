"""Balance check for Talent Stack: Data Science Edition.

Scores every possible 3-card team for every Quest x Market Event x Secret Company
combination and reports whether the full required lineup is still the best plan.

Design rule being checked: completing the quest must always score best or tied-best.

Run:  python balance_check.py
Edit the CAREERS / QUESTS / MARKETS / COMPANIES tables below when cards change,
and keep them in sync with ../cards.html.
"""
import itertools
import math
from collections import Counter

# name: (median salary in $1,000s, tech stack icons, degree points, tier 1-3)
CAREERS = {
    "Data Analyst": (82, {"SQL", "Tableau"}, 1, 1),
    "Machine Learning Engineer": (140, {"Python", "Cloud"}, 1, 3),
    "Data Engineer": (125, {"SQL", "Cloud"}, 1, 2),
    "Chief Data Officer": (190, {"SQL", "Security"}, 2, 3),
    "AI Research Scientist": (150, {"Python", "Tableau"}, 2, 3),
    "Cybersecurity Data Analyst": (102, {"SQL", "Security"}, 1, 2),
    "Bioinformatics Specialist": (108, {"Python", "SQL"}, 1, 2),
    "Sports Analytics Specialist": (88, {"Tableau", "Python"}, 1, 1),
    "Game Data Analyst": (92, {"SQL", "Tableau"}, 1, 1),
    "Climate Data Scientist": (112, {"Python", "Cloud"}, 2, 2),
    "Social Media Data Analyst": (78, {"Tableau", "SQL"}, 1, 1),
    "Healthcare Data Scientist": (118, {"Python", "Security"}, 2, 2),
}

# quest: (required roles, budget cap in $1,000s)
QUESTS = {
    "1 Autonomous School Transit Network": (["Data Engineer", "Machine Learning Engineer", "Cybersecurity Data Analyst"], 370),
    "2 Video Game Engagement & Economy Engine": (["Game Data Analyst", "Data Engineer", "Machine Learning Engineer"], 360),
    "3 Global Climate Prediction Platform": (["Climate Data Scientist", "Data Engineer", "Bioinformatics Specialist"], 350),
    "4 Pro League Draft Predictor": (["Sports Analytics Specialist", "AI Research Scientist", "Data Analyst"], 325),
    "5 Hospital Early-Warning System": (["Healthcare Data Scientist", "Cybersecurity Data Analyst", "AI Research Scientist"], 375),
    "6 Viral Video Trend Tracker": (["Social Media Data Analyst", "Data Analyst", "Machine Learning Engineer"], 305),
    "7 School District Data Makeover": (["Chief Data Officer", "Data Analyst", "Cybersecurity Data Analyst"], 380),
    "8 Outbreak Tracker": (["Healthcare Data Scientist", "Bioinformatics Specialist", "Social Media Data Analyst"], 310),
    "9 Esports League Launch": (["Game Data Analyst", "Sports Analytics Specialist", "Chief Data Officer"], 375),
    "10 Wildfire Alert App": (["Climate Data Scientist", "Social Media Data Analyst", "AI Research Scientist"], 345),
    "11 Global Food Forecast": (["Climate Data Scientist", "Bioinformatics Specialist", "Chief Data Officer"], 415),
    "12 Youth Fitness Game App": (["Game Data Analyst", "Sports Analytics Specialist", "Healthcare Data Scientist"], 305),
}


def has(icon):
    return lambda c: icon in CAREERS[c][1]


# Market effects: sal = salary change per card, cap = budget cap change, bonus = +1 per matching card (max +2),
# synplus = extra synergy points, pen = points lost per $10k over, max3 = most $$$ roles allowed.
MARKETS = {
    "Steady Market": {},
    "AI Boom": {"sal": lambda c: 10 if has("Python")(c) else 0, "cap": 20},
    "Cloud Sale": {"sal": lambda c: -10 if has("Cloud")(c) else 0},
    "Cyberattack!": {"bonus": has("Security")},
    "Dashboard Craze": {"bonus": has("Tableau")},
    "Internship Program": {"sal": lambda c: -10 if CAREERS[c][3] == 1 else 0},
    "Talent Shortage": {"sal": lambda c: 15 if CAREERS[c][3] == 3 else 0, "cap": 15},
    "Investor Bonus": {"cap": 30},
    "Hiring Freeze": {"max3": 1},
    "Open Source Week": {"synplus": 1},
    "Audit Season": {"pen": 2},
    "Grad Rush": {"sal": lambda c: -5 if CAREERS[c][2] == 1 else 0},
}

# Secret Company bonus at final scoring (never above +2). Args: team, total payroll.
COMPANIES = {
    "Startup": lambda t, pay: 2 if pay <= 300 else 0,
    "Big Tech": lambda t, pay: 2 if any(CAREERS[c][3] == 3 for c in t) else 0,
    "Nonprofit": lambda t, pay: min(2, sum(CAREERS[c][3] == 1 for c in t)),
    "Research Lab": lambda t, pay: 2 if sum(CAREERS[c][2] for c in t) >= 5 else 0,
    "Security Firm": lambda t, pay: 2 if any(has("Security")(c) for c in t) else 0,
    "Creative Studio": lambda t, pay: 2 if any(has("Tableau")(c) for c in t) else 0,
    "Cloud Company": lambda t, pay: 2 if sum(has("Cloud")(c) for c in t) >= 2 else 0,
    "Mid-Size Agency": lambda t, pay: 2 if sorted(CAREERS[c][3] for c in t) == [1, 2, 3] else 0,
}


def score(team, required, cap, market, company):
    """Audit score plus company bonus, or None if the market makes the team illegal."""
    if sum(CAREERS[c][3] == 3 for c in team) > market.get("max3", 3):
        return None
    missing = [r for r in required if r not in team]
    points = 5 * (3 - len(missing))  # role match
    extras = [c for c in team if c not in required]
    for role in missing:  # stand-ins: one shared tech icon, one role per card
        for card in extras:
            if CAREERS[card][1] & CAREERS[role][1]:
                points += 1
                extras.remove(card)
                break
    salary = market.get("sal", lambda c: 0)
    payroll = sum(CAREERS[c][0] + salary(c) for c in team)
    cap += market.get("cap", 0)
    points += 3 if payroll <= cap else -market.get("pen", 1) * math.ceil((payroll - cap) / 10)
    shared = max(Counter(i for c in team for i in CAREERS[c][1]).values())
    points += {1: 0, 2: 1, 3: 3}[shared] + (market.get("synplus", 0) if shared > 1 else 0)
    if "bonus" in market:
        points += min(2, sum(market["bonus"](c) for c in team))
    if company:
        points += COMPANIES[company](team, payroll)
    return points


def main():
    teams = list(itertools.combinations(CAREERS, 3))
    uses = Counter(r for req, _ in QUESTS.values() for r in req)
    print("Quests requiring each role:", ", ".join(f"{r} {n}" for r, n in sorted(uses.items())))
    unused = set(CAREERS) - set(uses)
    if unused:
        print("WARNING: roles no quest requires:", ", ".join(sorted(unused)))
    print()
    problems = 0
    for quest, (required, cap) in QUESTS.items():
        full = tuple(c for c in CAREERS if c in required)
        beaten = ties = 0
        backups = set()
        for market in MARKETS.values():
            for company in [None, *COMPANIES]:
                results = [(score(t, required, cap, market, company), t) for t in teams]
                results = [r for r in results if r[0] is not None and r[1] != full]
                full_score = score(full, required, cap, market, company)
                best = max(s for s, _ in results)
                beaten += full_score is None or best > full_score
                ties += best == full_score
                backups.add(frozenset(t for s, t in results if s == best))
        combos = len(MARKETS) * (len(COMPANIES) + 1)
        total = sum(CAREERS[r][0] for r in required)
        flag = "OK " if beaten == 0 else "FIX"
        print(f"{flag} Quest {quest}: lineup ${total}k, cap ${cap}k | beaten {beaten}/{combos}, "
              f"tied {ties}/{combos}, {len(backups)} different best backup plans")
        problems += beaten
    print("\nAll quests pass: completing the quest is always best or tied-best." if problems == 0
          else f"\n{problems} combinations where skipping a required role wins. Retune before printing.")


if __name__ == "__main__":
    main()
