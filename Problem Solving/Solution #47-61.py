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

#51. 
#52. 
#53. 
#54. 
#55. 
#56. 
#57. 
#58. 
#59. 
#60. 
#61. 
