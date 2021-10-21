for t in range(int(input())):
    n = int(input())
    L = [int(s) for s in input().split()]
    R = [int(s) for s in input().split()]
    Index = []
    for i in range(n):
        Index.append( (L[i] * R[i] , R[i], i) )

    Result = sorted(Index, key = lambda e: (e[0], e[1], n-e[2]), reverse = True)
    print(Result[0][-1]+1)

