for _ in range(int(input())):
    n, a, b = [int(s) for s in input().split()]
    sarthak = 0
    anuradha = 0
    for i in range(n):
        word = input()
        if(word[0] in "EQUINOX"):
            sarthak+=a
        else:
            anuradha+=b
    if(sarthak > anuradha):
        print("SARTHAK")
    elif(sarthak == anuradha):
        print("DRAW")
    else:
        print("ANURADHA")