def hitungLingkaran(bil):
    if bil == 0: 
       return "masukan jadi jari yang benar"
    else:
        keliling = 3.14 * bil * 2
        luas = 3.14 * bil * bil
        print(f"keliling lingkaran = {keliling}")
        print(f"luas lingkaran = {luas}")

bilangan = float(input("Masukan jaru jari : "))
hitungLingkaran(bilangan)
