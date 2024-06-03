def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Daftar nama anggota organisasi
anggota = ["Pain", "Konan", "Tobi", "Zetsu", "Sasori", "Hidan", "Deidara", "Kisame", "Kakuzu", "Itachi"]

# Mengurutkan nama anggota menggunakan algoritma Selection Sort
selectionSort(anggota)

# Menampilkan nama anggota yang sudah diurutkan
print("Nama anggota organisasi setelah diurutkan:")
for nama in anggota:
    print(nama)
