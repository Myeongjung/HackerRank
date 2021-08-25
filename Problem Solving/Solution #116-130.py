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
	
#117. Climbing the Leaderboard
def climbingLeaderboard(ranked, player):
    result = []
    ranked = sorted(set(ranked), reverse=True)
    l = len(ranked)

    for a in player:
        while (l > 0) and (a >= ranked[l-1]):
            l -= 1
        result.append(l+1)
    return result
	
#118. Extra Long Factorials
def extraLongFactorials(n):
    result = 1
    while n > 0:
        result *= n
        n-=1
    print(result)
	
#119. Non-Divisible Subset
def nonDivisibleSubset(k, s):
    counts = [0] * k
    for number in s:
        counts[number % k] += 1

    count = min(counts[0], 1)
    for i in range(1, k//2+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
    if k % 2 == 0: 
        count += 1
        
    return count
	
#120. Queen's Attack II
def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = {(ob[0],ob[1]) for ob in obstacles}

    mvs, count = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)], 0

    for m in mvs:
        cr, cc = r_q, c_q
        while (cr + m[0] >= 1 and cr + m[0] <= n) and (cc + m[1] >= 1 and cc + m[1] <= n):
            cr += m[0]
            cc += m[1]
            if (cr, cc) in obstacles:break
            count += 1

    return count

