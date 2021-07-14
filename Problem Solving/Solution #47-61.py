#47. Halloween Sale
def howManyGames(p, d, m, s):
    count = 0
    while s - p >= 0:
        s -= p
        count += 1
        p = max(p-d,m);
    return count
	
#48. Chocolate Feast
def chocolateFeast(n, c, m):
    choco, eat, wp=n//c, 0, 0
    while choco>0:
        eat+=choco
        wp+=choco
        choco = wp // m
        wp = wp % m
    return eat

#49. Service Lane
def serviceLane(width, cases):
    result = []
    for i,j in cases:
        result.append(min(width[i:j+1]))
        
    return result

#50. Lisa's Workbook
def workbook(n, k, arr):
    count = 0
    page = 0
    for i in arr:
        for j in range(1,i+1):
            print(j)
            if k == 1 or j%k == 1:
                page+=1
            if j == page:
                count+=1
    return count

#51. Flatland Space Stations
def flatlandSpaceStations(n, c):
    c.sort()
    result = max(c[0], n-1 - c[-1])
    for i in range(len(c)-1):
        result = max((c[i+1]-c[i])//2, result)
    return result

#52. Fair Rations
def fairRations(B):
    idx = [i for i, x in enumerate(B) if x % 2 == 1 ]
    return "NO" if len(idx) % 2 == 1 else str(sum([(idx[i+1]-idx[i])*2 for i in range(0,len(idx),2)]))

#53. Cavity Map
def cavityMap(grid):
    n = len(grid) - 1
    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] > max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):               
				grid[i] = grid[i][:j] +'X' + grid[i][j+1:]
    return grid 

#54. Manasa and Stones


#55. 
#56. 
#57. 
#58. 
#59. 
#60. 
#61. 
