#89. The Love-Letter Mystery
def theLoveLetterMystery(s):
    front = s[:len(s)//2]
    back = s[len(s)//2:] if len(s)%2==0 else s[(len(s)//2)+1:]
    back = back[::-1]
    count = 0
    
    for i in range(len(front)):
        count += abs(ord(front[i]) - ord(back[i]))
    return count

#90. Find the Median
def findMedian(arr):
    return sorted(arr)[len(arr)//2]


