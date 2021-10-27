import time
start = time.time()

array = []
num = int(input("Enter the Size of Array: "))

for i in range(num):
    digits = int(input("Enter the Digits you want to sort: "))
    array.append(digits)

def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    print("The Selection Sort is : ", arr)
    
time.sleep(1)
stop = time.time()

print(f"The Time taken for Selection Sort {stop - start}")     
SelectionSort(array)