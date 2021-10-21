for _ in range(int(input())):
    amount = int(input())
    notes = 0
    denominations = [100, 50, 10, 5, 2, 1]
    for deno in denominations:
        notes += (amount // deno)
        amount = amount % deno
    print(notes)