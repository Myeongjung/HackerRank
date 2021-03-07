for _ in range (int(input())):
    s = input()
    l = len(s)
    odd,even = "", ""
    for i in range(l):
        if i % 2 != 0:
            even += s[i]
        else:
            odd += s[i]
            
    print(odd, even)