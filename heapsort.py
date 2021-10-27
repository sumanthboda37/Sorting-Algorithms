import time
start = time.time()

array = []
num = int(input("Enter the Size of Array: "))

for i in range(num):
    digits = int(input("Enter the Digits you want to sort: "))
    array.append(digits)
    
def Heapify(arr,length,i):
    large = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < length and arr[large] < arr[left]:
        large = left
    
    if right < length and arr[large] < arr[right]:
        large = right
        
    if large != i:
        temp = arr[i]
        arr[i] = arr[large]
        arr[large] = temp
        #arr[i], arr[large] = arr[large], arr[i]       
        Heapify(arr, length, large)
    
def HeapSort(arr):
    length = len(arr)
    
    for i in range (length//2 - 1, -1, -1):
        Heapify(arr, length, i)
    
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)             
    print("The Heap Sort is : ", arr)
    
time.sleep(1)
stop = time.time()

print(f"The Time taken for Heap Sort is {stop - start}")
    
HeapSort(array)