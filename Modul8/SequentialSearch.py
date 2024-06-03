def sequential_search(database, target):
    for plat_nomor in database:
        if plat_nomor == target:
            return True
    return False

database_plat_nomor = ["R 300 SR", "R 1234 DJ", "R 701 LP", "R 3218 RR", "R 007 TU",
                       "R 3 ST", "R 999 RT", "R 210 RO", "R 1111 II", "R 4987 LH"]

nomor_plat_cari = "R 999 RS"

hasil_pencarian = sequential_search(database_plat_nomor, nomor_plat_cari)

if hasil_pencarian:
    print(f"Nomor plat mobil {nomor_plat_cari} ditemukan dalam database.")
else:
    print(f"Nomor plat mobil {nomor_plat_cari} tidak ditemukan dalam database.")
