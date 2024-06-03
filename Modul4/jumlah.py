bilangan = int(input("Masukkan Bilangan: "))
jumlah = 0
nilai_string = ""

for i in range(1, bilangan + 1):
    jumlah += i
    if i != bilangan:
        nilai_string += f"{i} + "
    else:
        nilai_string += f"{i}"

print(f"Total nilai = {nilai_string} = {jumlah}")
