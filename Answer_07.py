for _ in range(int(input())):
    a, b, c, d = [int(s) for s in input().split()]
    if( (a+c) == (b+d) ):
        print("YES")
    else:
        print("NO")