def operasi(pilihan1):
	switcher = {
		1: "JENIS PENYAKIT MATA\n1. Katarak\n2. Plus/Minus\n3. Silinder",
		2: "JENIS PENYAKIT JANTUNG\n1. Jantung Koroner\n2. Katup Jantung\n3. Otot Jantung",
	}
	return switcher.get(pilihan1)

katarak = "Rp. 7.500.000"
minus = "Rp. 5.000.000"
silinder = "Rp. 4.000.000"
koroner = "Rp. 500.000.000"
katup = "Rp. 350.000.000"
otot = "Rp. 450.000.000"

print("<-- MENU HITUNG BIAYA OPERASI -->\n1. Hitung biaya operasi mata\n2. Hitung biaya operasi jantung")
pilihan = int(input("masukan pilihan : "))

if pilihan == 1:
	print (operasi(1))
	pilih = int(input("Masukan Jenis Penyakit Mata : "))
	if pilih ==1:
		print(f"biaya operasi mata katarak = {katarak}")
	elif pilih == 2:
		print(f"biaya operasi mata plus/minus = {minus}")
	elif pilih == 3:
		print(f"biaya operasi mata silinder = {silinder}")
	else:
		print("masukan pilihan yang benar")
elif pilihan == 2:
	print(operasi(2))
	pilih = int(input("Masukan Jenis Penyakit Jantung : "))
	if pilih ==1:
		print(f"biaya operasi jantung koroner = {koroner}")
	elif pilih == 2:
		print(f"biaya operasi katup jantung = {katup}")
	elif pilih == 3:
		print(f"biaya operasi otot jantung = {otot}")
	else:
		print("masukan pilihan yang benar")
else :
	print("masukan pilihan yang tepat")