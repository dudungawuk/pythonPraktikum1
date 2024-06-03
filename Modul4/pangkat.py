bilangan = int(input("masukan bilangan : "))
pencacah = int(input("masukan pencacah : "))
jumlah = 1

for i in range(1,pencacah+1):
    jumlah *= bilangan

print(jumlah)