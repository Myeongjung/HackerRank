r_d, r_m, r_y = map(int,input().split())
d, m, y = map(int,input().split())

if r_y < y:
    print(0)
else:
    if r_y - y >= 1:
        print(10000)
    elif r_m - m >= 1:
        print("{}".format((r_m-m)*500))
    elif r_d - d >= 1:
        print("{}".format((r_d-d)*15))
    else:
        print(0)