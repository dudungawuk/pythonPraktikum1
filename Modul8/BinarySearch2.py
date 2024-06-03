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

nim_mahasiswa = [12102001, 12102002, 12102003, 12102004, 12102005,
                 12102006, 12102007, 12102008, 12102009, 12102010,
                 12102011, 12102012, 12102013]

nim_cari = 12102001

hasil_pencarian = binary_search(nim_mahasiswa, nim_cari)

if hasil_pencarian:
    print(f"NIM {nim_cari} ditemukan dalam kelas tersebut.")
else:
    print(f"NIM {nim_cari} tidak ditemukan dalam kelas tersebut.")
