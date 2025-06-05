def solve(q=[], row=0):
    if row == 8:
        print(q)
        for i in q:
            print('.' * i + 'Q' + '.' * (7 - i))

        return True
    for col in range(8):
        if all(col != c and abs(row - r) != abs(col - c)
                for r, c in enumerate(q)):
            if solve(q + [col], row + 1): 
                return True

solve()
