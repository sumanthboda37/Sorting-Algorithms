import time
start = time.time()

array = []
num = int(input("Enter the Size of Array: "))

for i in range(num):
    digits = int(input("Enter the Digits you want to sort: "))
    array.append(digits)

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    print("The BubbleSort is :" , arr)
time.sleep(1)
stop = time.time()

print(f"The Time taken for BubbleSort is {stop - start}")   
BubbleSort(array)