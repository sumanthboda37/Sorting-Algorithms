import time
start = time.time()

array = []
num = int(input("Enter the Size of Array: "))

for i in range(num):
    digits = int(input("Enter the Digits you want to sort: "))
    array.append(digits)
    
def MergeSort(arr):
    length = len(arr)
    if length > 1:
        middle = length//2
        left = arr[:middle]
        right = arr[middle:]
        MergeSort(left)
        MergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    print("The Merge Sort is : ", arr) 

time.sleep(1)
stop = time.time()
           
print(f"The Time taken for Merge Sort is {stop - start}") 
    
MergeSort(array)