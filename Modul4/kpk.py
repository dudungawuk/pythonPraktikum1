def hitung_fpb(a, b):
    while b:
        a, b = b, a % b
    return a

def hitung_kpk(a, b):
    return (a * b) // hitung_fpb(a, b)

# Contoh penggunaan
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

kpk = hitung_kpk(bil1, bil2)
print(f"KPK dari {bil1} dan {bil2} adalah: {kpk}")
