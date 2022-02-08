



#task 2
#def return_element_index(lst, search):
#    for index, element in enumerate(lst):
#        if element == search:
    # #       return index
      #  return -1


#test_list = [0, 2, 4, 3, 5, 'asd']

#print(return_element_index(test_list, '0'))
#print(return_element_index(test_list, 0))
#print(return_element_index(test_list, 'asd'))


#task 4
#def fun(lst):
#print(lst.sort()[:5])

#task 7
#def fun(lst):
 #   tmp = set()
 #   res = []
 #   for element in lst:
    #    if element not in tmp:
      #      res.append(element)
   #     tmp.add(element)
   # return res

#lst = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5 ]
#print(fun(lst))


#task 1
def sort(arr):
    quick_sort(arr, 0, len(arr) -1)
    
def quick_sort(array, low, high):
    if not array:
        return
    
    if low >= high:
        return
    
    middle = low + (high - low) // 2
    m = array[middle]
    
    i = low
    j = high
    while i <= j:
        while array[i] < m:
            i += 1
        while array[j] > m:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array [i]
            i += 1
            j -= 1
            
    if low < j:
        quick_sort(array, low, j)
    if high > i:
        quick_sort(array, i, high)
        
a = [1, 6, 8, 5467, 234, 612, 565787]
sort(a)
print(a)

#task 6
a = input('Введіть число: \n')
print((lambda x: sum(x) / len(x))((*map(int, input().split()),)))
