def a_star(graph, heuristics, start, goal):
    open_list = [(start, [start], 0)] 
    
    while open_list:
        open_list.sort(key=lambda x: x[2] + heuristics[x[0]]) 
        current, path, cost = open_list.pop(0)

        if current == goal:
            return path

        for neighbor, weight in graph.get(current, []):
            open_list.append((neighbor, path + [neighbor], cost + weight))

    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 3)],
    'C': [('E', 5)],
    'D': [('F', 2),('G',4)],
    'E': [('G', 3)], 'F': [('G',1)]
}
heuristics = {
    'A': 5, 'B': 6, 'C': 4,
    'D': 3, 'E': 3, 'F': 1, 'G':0
}
result = a_star(graph, heuristics, 'A', 'G')
print("A* Path:", result)

