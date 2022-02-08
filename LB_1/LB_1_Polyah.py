import math

a = input('Введіть число х: \n')
a = int(a)
z = math.cos(a) ** math.e - math.sqrt(a)
print(z)

import random

N = int(input("Введіть число: "))
arr = []

for i in range(0, N):
    arr.append(random.randint(-10, 10))

print(arr)

 
mul = 1
index = len(arr) - 1
mi = float('inf')
while index >= 0:
    if arr[index] < 0 and arr[index] < mi:
        mi = arr[index]
    if arr[index] != 0 and arr[index] % 3 == 0:
        mul *= arr[index]
    if arr[index] < 0:
        print('Відємні елементи:' + str(arr[index]))
    index -= 1

print(f'Мінімальний відємний: {mi}')
print(f'Добуток ненульових: {mul}')


M = int(input("Ціле число:"))
minN = 0
k = 0
while k <= M:
    if 3 * k > M:
        if minN < 1:
            minN -= 1
    k += 1
print("M = " + str(minN))