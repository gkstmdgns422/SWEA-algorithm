import sys
sys.stdin = open('sample_input.txt')

# 1번째 풀이
# T = int(input())
# for tc in range(1, T + 1):
#     words = [list(input()) for _ in range(5)]
#     word = ''
#
#     for i in range(15):
#         for j in range(5):
#             try:
#                 word += words[j][i]
#             except:
#                 pass
#     print('#{} {}'.format(tc, word))

T = int(input())
for tc in range(1, T + 1):
    words = [list(input()) for _ in range(5)]
    word = ''

    for i in range(15):
        for j in range(5):
            if len(words[j]) > i:
                word += words[j][i]

    print('#{} {}'.format(tc, word))



