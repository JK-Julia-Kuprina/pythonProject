# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом.Определите минимальное число монеток, которые
# нужно перевернуть, чтобы все монетки был повернуты вверх  и той же стороной.Выведите
# минимальное количество монет, которые нужно перевернуть

import random

from random import randint

n = int(input("Введите количество монеток: "))
tails = 0
eagle = 0
coins = [0, 1]
for i in range(n):

    random.shuffle(coins)
    print(f'все монеты {coins}')

    if int(coins[0]) == 0:
        eagle += 1
    if int(coins[0]) == 1:
        tails += 1
print(f'всего монеток{tails, eagle}')

if tails > eagle:
    turn = eagle
else:
    turn = tails
print(f'минимальное количество монет, которые надо перевернуть {turn}')

