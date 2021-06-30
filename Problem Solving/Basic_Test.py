#String Anagram

def stringAnagram(dictionary, query):
    dict={}
    for s in dictionary:
        i=str(sorted(s))
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    ans=[]
    for s in query:
        i=str(sorted(s))
        if i in dict:
            ans.append(dict[i])
        else:
            ans.append(0)
    return ans