# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


# N = int(input())
# i = 1
# while i <= N:
#     if i < N:
#         if i * 2 > N:
#             break
#         else:
#             i = i * 2
#             print(i)

n = int(input())
i = 1
num = 0
while i < n:
    print(2 ** num, end=' ')
    i *= 2
    num += 1
