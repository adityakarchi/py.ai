def tsp_nn(mat):
    n, v, p, d, c = len(mat), [0], [False]*len(mat), 0, 0
    p[0] = True
    while len(v) < n:
        j = min((i for i in range(n) if not p[i]), key=lambda x: mat[c][x])
        d += mat[c][j]
        v.append(j)
        p[j], c = True, j
    return v + [0], d + mat[c][0]

mat = [[0, 20, 40, 22], [20, 0, 13, 30], [40, 13, 0, 12], [22, 30, 12, 0]]
path, cost = tsp_nn(mat)
print("Path:", path)
print("Total distance:", cost)
