#116. Forming a Magic Square
def formingMagicSquare(s):
    solution = [[8,3,4],[1,5,9],[6,7,2]]
    cost = float('inf')

    for _ in range(4):
        diff = sum([abs(s[i][j] - solution[i][j]) for i in range(len(s)) for j in range(len(s))])
        cost = min(cost, diff)
        flipped = [i[::-1] for i in solution]
        diff = sum([abs(s[i][j] - flipped[i][j]) for i in range(len(s)) for j in range(len(s))])
        cost = min(cost, diff)
        solution = [list(i) for i in zip(*solution[::-1])]

    return cost
	

