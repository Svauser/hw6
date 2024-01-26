def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print (selectionSort([3,2,0,18,55,35,68,99,2102,75,20,10,17,94]))

def binary_search(list, my_num):
    low_ind =0
    high_ind = len(list)-1
    while low_ind <= high_ind :
        midle = (low_ind + high_ind)//2
        guess = list[midle]
        if guess == my_num:
            return midle
        if guess > my_num:
            high_ind = midle - 1
        else:
            low_ind = midle + 1
    return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(binary_search(my_list,10))
print(binary_search(my_list,-1))