# List data
penyewaan_list = []

# Main Menu
def sewa():
    while True:
        print("========================================")
        print("=== Sistem Penyewaan Lapangan Futsal ===")
        print("=====      By Endrawan Radhitya    =====")
        print("========================================\n")
        print("1. Tambah Penyewaan ")
        print("2. Lihat Penyewaan ")
        print("3. Update Penyewaan")
        print("4. Hapus Penyewaan ")
        print("5. Sorting penyewa")
        print("6. Mencari penyewa")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            create()
        elif pilihan == "2":
            read()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            sorting()
        elif pilihan == "6":
            search()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-7.")

# Fungsi Create
def create():
    if len(penyewaan_list) >= 3:
        print("Lapangan sedang penuh.")
        return
    try:
        nama = input("Masukkan nama penyewa: ")
        if not nama:
            print("Error: Nama penyewa tidak boleh kosong.")
            return
        lama_sewa = int(input("Masukkan lama penyewaan (dalam jam): "))
        if lama_sewa <= 0:
            print("Error: Lama penyewaan harus berupa angka positif.")
            return
        harga = lama_sewa * 100000
        penyewaan = [nama,lama_sewa,harga]
        penyewaan_list.append(penyewaan)
        print("Penyewaan berhasil ditambahkan:")
        print(f"Nama: {penyewaan[0]} Lama Sewa: {penyewaan[1]} jam Harga: Rp{penyewaan[2]}")
    except ValueError:
        print("Error: Lama penyewaan harus berupa angka bulat.")

# Fungsi Read
def read():
    if not penyewaan_list:
        print("Tidak ada data penyewaan.")
        return
    print("Daftar Penyewaan:")
    for i, penyewaan in enumerate(penyewaan_list, start=1):
        print(f"{i}. Nama: {penyewaan[0]} Lama Sewa: {penyewaan[1]} jam Harga: Rp{penyewaan[2]}")

# Fungsi Update
def update():
    if not penyewaan_list:
        print("Tidak ada data penyewaan untuk diupdate.")
        return
    read()
    try:
        index = int(input("Masukkan nomor penyewaan yang ingin diupdate: ")) - 1
        if index < 0 or index >= len(penyewaan_list):
            print("Nomor penyewaan tidak valid.")
            return
        nama = input("Masukkan nama penyewa baru: ")
        if not nama:
            print("Error: Nama penyewa tidak boleh kosong.")
            return
        lama_sewa = int(input("Masukkan lama penyewaan baru (dalam jam): "))
        if lama_sewa <= 0:
            print("Error: Lama penyewaan harus berupa angka positif.")
            return
        harga = lama_sewa * 100000
        penyewaan_list[index] = [nama, lama_sewa, harga]
        print("Penyewaan berhasil diupdate:")
        print(f"Nama: {nama} Lama Sewa: {lama_sewa} jam Harga: Rp{harga}")
    except ValueError:
        print("Error: Input tidak valid.")

#Fungsi Delete
def delete():
    if not penyewaan_list:
        print("Tidak ada data penyewaan untuk dihapus.")
        return
    read()
    try:
        index = int(input("Masukkan nomor penyewaan yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(penyewaan_list):
            print("Nomor penyewaan tidak valid.")
            return
        hapus = penyewaan_list.pop(index)
        print("Penyewaan berhasil dihapus:")
        print(f"Nama: {hapus[0]} Lama Sewa: {hapus[1]} jam Harga: Rp{hapus[2]}")
    except ValueError:
        print("Error: Input tidak valid.")

# Fungsi Sorting
def sorting():
    if not penyewaan_list:
        print("Tidak ada data penyewaan untuk diurutkan.")
        return
    print("Pilih jenis pengurutan:")
    print("1. Dari tersingkat ke terlama")
    print("2. Dari terlama ke tersingkat")
    pilihan = input("Masukkan pilihan (1 atau 2): ")
    
    if pilihan not in ["1", "2"]:
        print("Pilihan tidak valid. Silakan coba lagi.")
        sorting()
        return
    
    n = len(penyewaan_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if pilihan == "1":
               if penyewaan_list[j][1] > penyewaan_list[j + 1][1]:
                  penyewaan_list[j], penyewaan_list[j + 1] = penyewaan_list[j + 1], penyewaan_list[j]
            else:
                if penyewaan_list[j][1] < penyewaan_list[j + 1][1]:
                   penyewaan_list[j], penyewaan_list[j + 1] = penyewaan_list[j + 1], penyewaan_list[j]
    
    if pilihan == "1":
        print("Penyewaan berhasil diurutkan berdasarkan lama sewa (dari tersingkat ke terlama).")
    else:
        print("Penyewaan berhasil diurutkan berdasarkan lama sewa (dari terlama ke tersingkat).")
    read()

# Fungsi Searching
def search():
    if not penyewaan_list:
        print("Tidak ada data penyewaan untuk dicari.")
        return
    cari = input("Masukkan nama penyewa yang ingin dicari: ")
    if not cari:
        print("Error: Nama penyewa tidak boleh kosong.")
        return
    hasil = []
    for penyewaan in penyewaan_list:
        if cari in penyewaan[0]:
            hasil.append(penyewaan)
    if hasil:
        print("Hasil pencarian:")
        for i, penyewaan in enumerate(hasil, start=1):
            print(f"{i}. Nama: {penyewaan[0]} Lama Sewa: {penyewaan[1]} jam Harga: Rp{penyewaan[2]}")
    else:
        print("Tidak ada penyewa dengan nama tersebut.")

sewa()
