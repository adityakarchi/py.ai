def water_jug_dfs(jug1, jug2, target):
    stack = [(0, 0, "Start")]
    visited = set()
    
    while stack:
        a, b, action = stack.pop()
        print(f"Action: {action} -> Jug1: {a}L, Jug2: {b}L")

        if a == target or b == target:
            print(f" Solution found: ({a}, {b})")
            return True

        if (a, b) in visited:
            continue
        
        visited.add((a, b))

        stack.extend([
            (jug1, b, "Filled Jug1"),
            (a, jug2, "Filled Jug2"),
            (0, b, "Emptied Jug1"),
            (a, 0, "Emptied Jug2"),
            (a - min(a, jug2 - b), b + min(a, jug2 - b), "Poured Jug1 → Jug2"),
            (a + min(b, jug1 - a), b - min(b, jug1 - a), "Poured Jug2 → Jug1")
        ])

    print(" No solution found.")
    return False

# Example usage
water_jug_dfs(5,3, 1)