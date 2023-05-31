def swap(arr, i, minPos):
    temp = arr[i]
    arr[i] = arr[minPos]
    arr[minPos] = temp

n = int(input("Enter NO. of elemetes : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element no. " + str(i+1) + " : ")))

for i in range(n):
    min = arr[i]
    minPos = i
    for j in range(i+1, n):
        if min > arr[j]:
            min = arr[j]
            minPos = j
    swap(arr, i, minPos)
    for j in range(n):
        print(arr[j], end=" ")
    print()
