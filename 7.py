def negate(lit):
    return lit[1:] if lit.startswith("~") else "~" + lit

def resolve(c1, c2):
    for a in c1:
        for b in c2:
            if a == negate(b):
                return list(set(c1 + c2) - {a, b})
    return None

def unify(clause):
    return [lit.replace("x", "Socrates")
             for lit in clause]

rules = [["~Man(x)", "Mortal(x)"]]
facts = ["Man(Socrates)"]
goal = "Mortal(Socrates)"
neg_goal = "~Mortal(Socrates)"

r = unify(rules[0])
step1 = resolve(r, facts)
print("Step 1:", step1)

step2 = resolve(step1, [neg_goal])
print("Step 2:", step2)

print("\nGoal Proven!" if step2 == [] else "\nGoal Not Proven")
