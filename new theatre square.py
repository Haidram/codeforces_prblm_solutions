def solve(nmxy, rect):
    n = nmxy[0]
    m = nmxy[1]
    x = nmxy[2]
    y = nmxy[3]

## To check if using 1x1 tile instead of 1x2
#  is cheaper or not
    if 2*x <= y:   
        count = 0
        for i in range(n):
            for j in rect[i]:
                if j == '.':
                    count += x
        return count

## Now using 1x2 tile wherever there is 2
#  consecutive white block in the same row
    else:
        count = 0
        for i in range(n):
            j = 0
            while j < m:
                if j < m-1:
                    if rect[i][j] == '.' and rect[i][j+1] == '.':
                        count += y
                        j += 2
                        continue
                if rect[i][j] == '.':
                    count += x
                    j += 1
                else:
                    j += 1
        return count



t = int(input())
for i in range(t):
    nmxy = list(map(int,input().strip().split()))[:4]
    rect = []
    for j in range(nmxy[0]):
        sq = input()
        rect.append(sq)
    print(solve(nmxy, rect))
