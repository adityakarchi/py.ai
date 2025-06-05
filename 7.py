rule = [["~Man(x)", "Mortal(x)"]]


facts = ["Man(Socrates)"]


goal = "Mortal(Socrates)"


negated_goal = "~Mortal(Socrates)"


clauses = rule[0] + [negated_goal] + facts


def resolve(clause1, clause2):
    for c1 in clause1:
        for c2 in clause2:
            if c1 == negate(c2):
                new_clause = list(set(clause1 + clause2))
                new_clause.remove(c1)
                new_clause.remove(c2)
                return new_clause
    return None

def negate(literal):
    if literal.startswith("~"):
        return literal[1:]
    else:
        return "~" + literal


def unify(clause):
    unified = []
    for lit in clause:
        unified.append(lit.replace("x", "Socrates"))
    return unified


rule_clause = unify(rule[0])
goal_clause = [negated_goal]
fact_clause = facts


step1 = resolve(rule_clause, fact_clause)
print("Step 1 Resolution:", step1)

step2 = resolve(step1, goal_clause)
print("Step 2 Resolution (goal):", step2)

if step2 == []:
    print("\n Goal Proven by Resolution!")
else:
    print("\nGoal Not Proven")



