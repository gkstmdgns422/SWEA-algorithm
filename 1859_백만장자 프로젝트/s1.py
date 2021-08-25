import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    benefit = 0
    for i in range(N-1,-1,-1):  # 거꾸로 이동
        if max_price > price[i]:
            benefit += max_price - price[i]
        else:
            max_price = price[i]
    print('#{} {}'.format(tc, benefit))