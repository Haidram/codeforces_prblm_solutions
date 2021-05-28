def whoWin(match,card):
    card = str(card)
    if match == 1:
        if (int(card))%2 == 0:
            return 2
        else:
            return 1
    elif match%2 == 0:
        i = 1
        while i < len(card):
            if (int(card[i]))%2 == 0:
                return 2
            i += 2
        return 1
    else:
        i = 0
        while i < len(card):
            if (int(card[i]))%2 != 0:
                return 1
            i += 2
        return 1
        

n = int(input())
for i in range(n):
    a = [0]*2
    for j in range(2):
        a[j] = int(input())
    num = whoWin(a[0],a[1])
    print(num)
