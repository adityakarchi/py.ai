rules = [(["cloudy"], "might_rain"), (["might_rain"], "take_umbrella")]
facts = {"cloudy"}
goal = "take_umbrella"

def forward(rules, facts, goal):
    while True:
        added = False
        for conds, concl in rules:
            if concl not in facts and all(c in facts for c in conds):
                facts.add(concl)
                print(f"Inferred: {concl}")
                if concl == goal:
                    return True
                added = True
        if not added: break
    return goal in facts

print("Goal reached:", forward(rules, facts, goal))
