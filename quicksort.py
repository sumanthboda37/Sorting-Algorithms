import time
start = time.time()

array = []
num = int(input("Enter the Size of array: "))

for i in range(num):
    digits = int(input("Enter the Digits you want to sort: "))
    array.append(digits)

def QuickSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    high = []
    low = []
    for item in arr:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)
    return QuickSort(low) + [pivot] + QuickSort(high)

print("Sorted Array:",QuickSort(array))

time.sleep(1)
stop = time.time()

print(f"The Time taken for Quick Sort is {stop - start}")