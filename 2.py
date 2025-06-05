from collections import deque

def is_valid(lm, lc, rm, rc):
    return all(x >= 0 for x in [lm, lc, rm, rc]) and \
           (lm == 0 or lm >= lc) and (rm == 0 or rm >= rc)

def successors(s):
    lm, lc, b, rm, rc = s
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    res = []
    for m, c in moves:
        if b:
            ns = (lm - m, lc - c, 0, rm + m, rc + c)
        else:
            ns = (lm + m, lc + c, 1, rm - m, rc - c)
        if is_valid(*ns[:2], *ns[3:]):
            res.append(ns)
    return res

def bfs(start, goal):
    q, seen = deque([(start, [start])]), set()
    while q:
        s, p = q.popleft()
        if s == goal: return p
        if s in seen: continue
        seen.add(s)
        q.extend((n, p + [n]) for n in successors(s) if n not in seen)
    return None

def solve():
    path = bfs((3,3,1,0,0), (0,0,0,3,3))
    print(*path, sep='\n') if path else print("No solution found.")

solve()
