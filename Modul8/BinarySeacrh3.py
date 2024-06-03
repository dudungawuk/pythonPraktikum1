def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

bilangan_acak = [21, 28, 37, 44, 52, 61, 68, 71, 72, 75]

angka_cari = 71

hasil_pencarian = binary_search(bilangan_acak, angka_cari)

if hasil_pencarian:
    print(f"Angka {angka_cari} ditemukan dalam daftar bilangan acak.")
else:
    print(f"Angka {angka_cari} tidak ditemukan dalam daftar bilangan acak.")
