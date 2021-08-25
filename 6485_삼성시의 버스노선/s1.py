import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    station = [0] * 5001
    AB = [0]
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    P = int(input())
    C = [0]
    for _ in range(P):
        C.append(int(input()))

    # 버스 정류장을 지나는 모든 노선들 체크
    for i in range(1, len(AB)):
        for j in range(AB[i][0], AB[i][1]+1):
            station[j] += 1
    ans = [0] * (P+1)
    for idx in range(1, P+1):
        ans[idx] = station[C[idx]]
    print('#{} '.format(tc), end='')
    print(*ans[1:])
