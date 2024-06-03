def cek(bil):
    if bil % 2 == 0:
        return "Bilangan yang Anda masukkan adalah bilangan Genap"
    else:
        return "Bilangan yang Anda masukkan adalah bilangan Ganjil"

bilangan = int(input("Masukkan Bilangan: "))
hasil = cek(bilangan)
print(hasil)
