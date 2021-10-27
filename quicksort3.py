import time
start = time.time()

array = []
num = int(input("Enter the Size of Array: "))

for i in range(num):
    digits = float(input("Enter the Digits you want to sort: "))
    array.append(digits)

def QuickSort(arr, ascend = True): 
    QuickOrder(arr, 0, len(arr), ascend)

def QuickOrder(L, low, high, ascend = True): 
    result = 0
    if low < high: 
        pivot_loc, result = Partition(L, low, high, ascend)  
        result += QuickOrder(L, low, pivot_loc, ascend)  
        result += QuickOrder(L, pivot_loc + 1, high, ascend)
    return result

def Median(arr, low, high):
    middle = (low+high-1)//2
    least = arr[low]
    medium = arr[middle]
    highest = arr[high-1]
    if least <= medium <= highest:
        return medium, middle
    if highest <= medium <= least:
        return medium, middle
    if least <= highest <= medium:
        return highest, high-1
    if medium <= highest <= least:
        return highest, high-1
    return least, low

def Partition(arr, low, high, ascend = True):
    print('Quicksort for 3 point median: ')
    print(arr)
    result = 0 
    pivot, index = Median(arr, low, high)
    arr[low], arr[index] = arr[index], arr[low]
    i = low + 1
    for j in range(low+1, high, 1):
        result += 1
        if (ascend and arr[j] < pivot) or (not ascend and arr[j] > pivot):
            arr[i], arr[j] = arr[j], arr[i]  
            i += 1
    arr[low], arr[i-1] = arr[i-1], arr[low] 
    return i - 1, result

arr_digits = list(array)

QuickSort(arr_digits, False)
print('sorted in Descending order:')
print(arr_digits)

time.sleep(1)
stop = time.time()

print(f"The Time taken for Quick Sort with 3 Median is {stop - start}")