def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Tukar posisi elemen jika elemen ke-j lebih besar dari elemen ke-(j+1)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Jika tidak ada pertukaran dilakukan pada iterasi ini, array sudah terurut
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

print("Array yang sudah diurutkan:")
for i in range(len(arr)):
    print(arr[i], end=" ")
