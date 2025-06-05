def ao_star(node, graph, heuristics, solution):
    if not graph.get(node):
        return heuristics[node]

    min_cost = float('inf')
    best_option = None

    for option in graph[node]:  
        cost = sum(1+heuristics[n] for n in option)
        if cost < min_cost:
            min_cost = cost
            best_option = option

    heuristics[node] = min_cost
    solution[node] = best_option

    for child in best_option:
        ao_star(child, graph, heuristics, solution)

    return heuristics[node]

def print_solution(node, solution):
    if node not in solution:
        print(node, end=" ")
        return
    print(node, "->", end=" ")
    for child in solution[node]:
        print_solution(child, solution)


graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G', 'H']],
    'E': [], 'F': [], 'G': [], 'H': []
}

heuristics = {
     'B': 5, 'C': 4, 'D': 7,
    'E': 3, 'F': 2, 'G': 1, 'H': 3
}

solution = {}
ao_star('A', graph, heuristics, solution)

print("AO* Solution Path:")
print_solution('A', solution)
