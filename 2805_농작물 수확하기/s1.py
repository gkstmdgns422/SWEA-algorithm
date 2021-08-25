import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n = N//2
    farm = [list(map(int, list(input()))) for _ in range(N)]

    ans = 0
    if len(farm) > 1:

        for i in range(N//2):
            ans += sum(farm[i][n-i:n+i+1])  # 위에서부터 아래로
            ans += sum(farm[N-1-i][n-i:n+i+1])  # 아래서부터 위로
        ans += sum(farm[n])  # 가운데
    else:
        ans = sum(farm[0])
    print('#{} {}'.format(tc, ans))
