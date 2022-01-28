#import math

#a = float(input("Enter a: "))
#z = math.cos(a) + math.cos(a * 2) + math.cos(a * 6) + math.cos(a * 7)

#print(z)

#n = int(input("Enter n: "))
#i = 0
#tmp = 2 * n - 1
#output = 1

#while i <= tmp:
#    if i % 2 != 0:
#        output *= i
#    i += 1

#print(output)

import random

N = int(input("Enter N: "))
arr = []

for i in range(0, N):
    arr.append(random.randint(-10, 10))

print(arr)

maxP = 0
sum = 0
j = 0
for i in arr:
    if arr[j] > maxP:
        maxP = arr[j]
    if arr[j] > 0:
        if arr[j] % 2 == 0:
            sum += arr[j]
    j += 1

k = -1
for i in arr:
    if arr[k] < 0:
        print("Element: " + str(arr[k]))
    k -= 1

print("suma = " + str(sum))
print("max = " + str(maxP))

