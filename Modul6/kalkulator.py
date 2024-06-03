def jumlah(bil1,bil2):
    jml = bil1 + bil2
    print(f"Hasil penjumlahan : {jml}")
def kurang(bil1,bil2):
    jml = bil1 - bil2
    print(f"Hasil pengurangan : {jml}")
def bagi(bil1,bil2):
    jml = bil1 / bil2
    if bil1 != 0:
        print(f"Hasil pembagian : {jml}")
    else:
        print("bilangan pertama tidak boleh 0!")
def kali(bil1,bil2):
    jml = bil1 * bil2
    print(f"Hasil pengalian : {jml}")
def pangkat(bil1,bil2):
    jml = 1
    for i in range(1,bil2+1):
        jml *= bil1
    return jml

print(jumlah)

print("KALKULATOR\n1. Penjumlahan\n2. Perkalian \n3. Pembagian \n4. Pengurangan \n5. Pangkat")
pilih = int(input("masukan pilihan : "))
if pilih in [1,2,3,4,5]:
    if pilih == 5:
        bilangan1 = int(input("Masukan bilangan : "))
        bilangan2 = int(input("Masukan bilangan pangkat : "))
        print(f"hasil pangkat : {pangkat(bilangan1,bilangan2)}")
    else:
        bilangan1 = int(input("Masukan bilangan pertama : "))
        bilangan2 = int(input("Masukan bilangan kedua : "))

    if pilih == 1 :
        jumlah(bilangan1,bilangan2)
    elif pilih == 2 :
        kali(bilangan1,bilangan2)
    elif pilih == 3 :
        bagi(bilangan1,bilangan2)
    elif pilih == 4 :
        kurang(bilangan1,bilangan2)
else: 
    print("Masukan pilihan yang benar!")