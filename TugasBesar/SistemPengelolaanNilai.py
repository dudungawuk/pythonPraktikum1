# Fungsi untuk menambahkan transaksi
def tambah_transaksi(transaksi_list, tipe, jumlah, deskripsi):
    transaksi = {
        'tipe': tipe,           # 'Pemasukan' atau 'Pengeluaran'
        'jumlah': jumlah,       # Jumlah uang
        'deskripsi': deskripsi  # Deskripsi transaksi
    }
    transaksi_list.append(transaksi)

# Fungsi untuk mencetak laporan keuangan
def cetak_laporan(transaksi_list):
    total_pemasukan = 0
    total_pengeluaran = 0
    
    print("Laporan Keuangan:")
    print("==========================================")
    print("{:<15} {:<10} {:<20}".format("Tipe", "Jumlah", "Deskripsi"))
    print("==========================================")
    
    for transaksi in transaksi_list:
        tipe = transaksi['tipe']
        jumlah = transaksi['jumlah']
        deskripsi = transaksi['deskripsi']
        
        if tipe == 'Pemasukan':
            total_pemasukan += jumlah
        elif tipe == 'Pengeluaran':
            total_pengeluaran += jumlah
            
        print("{:<15} {:<10} {:<20}".format(tipe, jumlah, deskripsi))
    
    saldo_akhir = total_pemasukan - total_pengeluaran
    
    print("==========================================")
    print(f"Total Pemasukan: {total_pemasukan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")
    print(f"Saldo Akhir: {saldo_akhir}")
    print("==========================================")

# Fungsi utama untuk mengelola buku kas
def main():
    transaksi_list = []
    
    while True:
        print("\n1. Tambah Pemasukan")
        print("\n2. Tambah Pengeluaran")
        print("\n3. Cetak Laporan Keuangan")
        print("\n4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            jumlah = float(input("Masukkan jumlah pemasukan: "))
            deskripsi = input("Masukkan deskripsi pemasukan: ")
            tambah_transaksi(transaksi_list, 'Pemasukan', jumlah, deskripsi)
        elif pilihan == '2':
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            deskripsi = input("Masukkan deskripsi pengeluaran: ")
            tambah_transaksi(transaksi_list, 'Pengeluaran', jumlah, deskripsi)
        elif pilihan == '3':
            cetak_laporan(transaksi_list)
        elif pilihan == '4':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
