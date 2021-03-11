n = int(input())
d = {}

for _ in range(n):
    name, number = input().split()
    d[name] = number
    
while True:
    try:
        name = input()
        if d.get(name):
            print("{}={}".format(name, d.get(name)))
        else:
            print("Not found")
    except:
        break