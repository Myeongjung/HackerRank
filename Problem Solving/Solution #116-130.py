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

#121. Organizing Containers of Balls
def organizingContainers(container):
    sv=[]
    sh=[]
    for i in range(n):
        sv.append(0)
        sh.append(sum(container[i]))
        for j in range(n):
            sv[i]+=container[j][i]
    sv.sort()
    sh.sort()
    return "Possible" if sv==sh else "Impossible"
	
#122. Bigger is Greater
def biggerIsGreater(w):
    arr = list(w)
    
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return "".join(arr)

#123. Encryption
def encryption(s):
    sm=s.replace(" ","")
    r=math.floor(math.sqrt(len(sm)))
    c=math.ceil(math.sqrt(len(sm)))
    ans = ""
    for i in range(c):
        ans += sm[i::c] + " "
    return ans
	
#124. Almost Sorted
def almostSorted(arr):
    sortedarr = sorted(arr)
    a = []
    subarr = []
    for i in range(len(arr)):
        if arr[i] != sortedarr[i]:
            a.append(i+1)
            
    if len(a) == 2:
        print("yes")
        print("swap", a[0],a[1],sep = " ")
    else:       
        for i in range(len(arr)):
            if arr[i] == sortedarr[i]:
                continue
            else:
                subarr.append(arr[i])
        if subarr == sorted(subarr,reverse = True):
            print("yes")
            print("reverse", arr.index(subarr[0])+1,arr.index(subarr[-1])+1,sep=" ")
        else:
            print("no")
			
#125. The Time in Words
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'half'}

def n2w(n):
    try:
        return(num2words[n])
    except KeyError:
        try:
            return(num2words[n-n%10] + " " + num2words[n%10]) 
        except KeyError:
            print('Number out of range')
            
def timeInWords(h, m):
    if m == 0:
        return "{} o' clock".format(n2w(h))
    elif m <= 30:
        return "{} past {}".format(n2w(m) + " minute" if m==1 else n2w(m) \
                if m==15 or m==30 else n2w(m) + " minutes", n2w(h))
    else:
        return "{} to {}".format(n2w(60-m) + " minute" if m==1 else n2w(60-m) \
                if 60-m==15 else n2w(60-m) + " minutes", n2w(h+1))
				
#126. Absolute Permutation
def absolutePermutation(n, k):
    if k == 0:
        return [i for i in range(1, n+1)]
    elif (n/k) % 2 != 0:
        return [-1]
    else:
        add = True
        perm = []
        
        for i in range(1, n+1):
            if add:
                perm.append(i+k)      
            else:
                perm.append(i-k)
                
            if i % k == 0:
                if add:
                    add = False
                else:
                    add = True
        return perm
		
#127. 
#128. 
#129. 
#130. 
