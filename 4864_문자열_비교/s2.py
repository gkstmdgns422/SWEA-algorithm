import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    p = input()
    t = input()
    if p in t:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))