import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]
    vortex = [[0] for _ in range(N)]
    u = 0
    for i in range(N):
        words = ''
        for j in range(N):
            #  90도
            words += matrix[N-1-j][i]
        vortex[u] = words
        words = ''
        for j in range(N):
            #  180도
            words += matrix[N-1-i][N-1-j]
        vortex[u] += ' ' + words
        words = ''
        for j in range(N):
            #  270도
            words += matrix[j][N-1-i]
        vortex[u] += ' ' + words
        u += 1
    print('#{}'.format(tc))
    for i in range(N):
        print(vortex[i])





