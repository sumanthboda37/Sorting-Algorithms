import time
start = time.time()

array = []
num = int(input("Enter the Size of Array: "))

for i in range(num):
    digits = int(input("Enter the Digits you want to sort: "))
    array.append(digits)
    
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("The Insertion sort is: ", arr)

time.sleep(1)
stop = time.time()

print(f"The Time taken for insertion Sort is {stop - start}")
    
InsertionSort(array)