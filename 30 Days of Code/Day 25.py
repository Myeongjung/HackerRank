for _ in range(int(input())):
    n = int(input())
    if(n == 1):
        print("Not prime")
    else:
        if(n % 2 == 0 and n > 2):
            print("Not prime")
        else:
            for i in range(3, int(n**(1/2))+1, 2):
                if n % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")