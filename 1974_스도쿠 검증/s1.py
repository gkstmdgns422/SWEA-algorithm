import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    sdq = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    for i in range(9):
        row = []
        col = []
        for j in range(9):
            if sdq[i][j] in row or sdq[j][i] in col:
                ans = 0
                break
            else:
                row.append(sdq[i][j])
                col.append(sdq[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nine = []
            for u in range(3):
                for v in range(3):
                    if sdq[i+u][j+v] in nine:
                        ans = 0
                        break
                    else:
                        nine.append(sdq[i+u][j+v])

    print('#{} {}'.format(tc, ans))


