import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [0] * 401
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        if start % 2 and end % 2:  # 홀수방 -> 홀수방
            for i in range(start, end+2):
                room[i] += 1
        elif start % 2 == 0 and end % 2:  # 짝수방 -> 홀수방
            for i in range(start-1, end+2):
                room[i] += 1
        elif end % 2 == 0 and start % 2:  # 홀수방 -> 짝수방
            for i in range(start, end+1):
                room[i] += 1
        else:  # 짝수방 -> 짝수방
            for i in range(start-1, end+1):
                room[i] += 1
    max_num = 0
    for num in room:
        if max_num < num:
            max_num = num
    print('#{} {}'.format(tc, max_num))

