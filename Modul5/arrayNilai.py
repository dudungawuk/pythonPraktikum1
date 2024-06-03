jmlmatkul = int(input("Masukkan jumlah mata kuliah: "))
nilai = []
print("")

for i in range(1, jmlmatkul + 1):
    input_nilai = int(input(f"Masukkan nilai mata kuliah ke-{i}: "))
    if input_nilai <= 100 :
        nilai.append(input_nilai)
    else :
        print("Nilai Tidak Valid!")
        exit()

print("")
total = 0

for nilai_matkul in nilai:
    total += nilai_matkul

rerata = total / jmlmatkul

if rerata < 100 and rerata >= 90 :
    print("Hasil Predikat A dengan nilai : ")
elif rerata >= 70:
    print("Hasil Predikat B dengan nilai : ")
elif rerata >= 50:
    print("Hasil Predikat C dengan nilai : ")
elif rerata >= 30:
    print("Hasil Predikat D dengan nilai : ")
elif rerata >= 0:
    print("Hasil Predikat E dengan nilai : ")

print("")
for index, nilai_matkul in enumerate(nilai):
    print(f"Nilai mata kuliah ke-{index} adalah {nilai_matkul}")

