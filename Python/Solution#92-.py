#92. The Minion Game

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowels = 'AEIOU'
    
    for i in range(len(string)):
        if s[i] in vowels:
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
		
#93. Merge the Tools!

def merge_the_tools(string, k):
    L = []
    for i in range(0,len(string),k):
        L = string[i:k+i]
        tmp = []
        for s in L:
            if (s not in tmp):
                tmp.append(s)
                
        print(''.join(tmp))
		
#94. 