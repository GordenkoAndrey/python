#task 3
#=========================================================================================
import random                                                                              #
                                                                                           #
N = int(input("Enter N: "))                                                                #
arr = []                                                                                   #
                                                                                           #
for i in range(0, N):                                                                      #
    arr.append(random.randint(-10, 10))   # ЭТО ШТАКА ДОБАВЛЯЕТ ЕЛЕМЕНТ В МАСИВ(РАНДОМНЫЙ) #
                                                                                           #
print(arr)                                                                                 #
                                                                                           #
maxP = 0                                                                                   #
sum = 0                                                                                    #
j = 0                                                                                      #
for i in arr:                                                                              #
    if arr[j] > maxP:                                                                      #
        maxP = arr[j]                                                                      #
    if arr[j] > 0:                                                                         #
        if arr[j] % 2 == 0:                                                                #
            sum += arr[j]                                                                  #
    j += 1                                                                                 #
                                                                                           #
k = -1                                                                                     #
for i in arr:                                                                              #
    if arr[k] < 0:                                                                         #
        print("Element: " + str(arr[k]))                                                   #
    k -= 1                                                                                 #
                                                                                           #
print("suma = " + str(sum))                                                                #
print("max = " + str(maxP))                                                                #
#===========================================================================================