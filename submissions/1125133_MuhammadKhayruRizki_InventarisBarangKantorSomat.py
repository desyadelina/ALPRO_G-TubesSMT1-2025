# Aplikasi Inventaris Barang Kantor Somat

inventaris = []

def create():
    print("\n=== TAMBAH BARANG BARU ===")
    kode = input("Kode Barang: ")
    if kode == "":
        print("Kode tidak boleh kosong!")
        return
    for barang in inventaris:
        if barang['kode'] == kode:
            print("Kode sudah ada!")
            return
    nama = input("Nama Barang: ")
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    kategori = input("Kategori: ")
    try:
        jumlah = int(input("Jumlah: "))
        if jumlah <= 0:
            print("Angka tidak boleh negatif dan 0!")
            return
    except:
        print("Harus berupa angka!")
        return
    lokasi = input("Lokasi: ")
    barang_baru = {
        'kode': kode,
        'nama': nama,
        'kategori': kategori,
        'jumlah': jumlah,
        'lokasi': lokasi
    }
    inventaris.append(barang_baru)
    print("Barang berhasil ditambahkan!")

def read():
    print("\n=== DAFTAR BARANG ===") 
    if len(inventaris) == 0:
        print("Belum ada barang di dalam inventaris.")
        return
    for i in range(len(inventaris)):
        print(f"\nBarang {i+1}:")
        print(f"Kode: {inventaris[i]['kode']}")
        print(f"Nama: {inventaris[i]['nama']}")
        print(f"Kategori: {inventaris[i]['kategori']}")
        print(f"Jumlah: {inventaris[i]['jumlah']}")
        print(f"Lokasi: {inventaris[i]['lokasi']}")
        print("---------------------")

def update():
    print("\n=== UPDATE BARANG ===")
    if len(inventaris) == 0:
        print("Belum ada barang di dalam inventaris.")
        return
    kode = input("Masukkan kode barang yang akan diupdate: ")
    ketemu = False
    for barang in inventaris:
        if barang['kode'] == kode:
            ketemu = True
            print(f"\nBarang ditemukan: {barang['nama']}")    
            nama_baru = input("Nama baru (enter jika tidak diubah): ")
            if nama_baru != "":
                barang['nama'] = nama_baru    
            kategori_baru = input("Kategori baru (enter jika tidak diubah): ")
            if kategori_baru != "":
                barang['kategori'] = kategori_baru  
            jumlah_baru = input("Jumlah baru (enter jika tidak diubah): ")
            if jumlah_baru != "":
                try:
                    barang['jumlah'] = int(jumlah_baru)
                    if jumlah_baru <= 0:
                        print("Angka tidak boleh negatif atau 0!")
                        return
                    elif jumlah_baru != "":
                        barang['jumlah'] = jumlah_baru
                except ValueError:
                    print("Jumlah tidak valid!")
                    return
            lokasi_baru = input("Lokasi baru (enter jika tidak diubah): ")
            if lokasi_baru != "":
                barang['lokasi'] = lokasi_baru
            print("Data barang berhasil diupdate.")
            break
    if not ketemu:
        print("Barang tidak ditemukan di inventaris.")

def delete():
    print("\n=== HAPUS BARANG ===")
    if len(inventaris) == 0:
        print("Belum ada barang di dalam inventaris.")
        return
    kode = input("Masukkan Kode Barang yang akan dihapus: ")
    for i in range(len(inventaris)):
        if inventaris[i]['kode'] == kode:
            print(f"Barang ditemukan: {inventaris[i]['nama']}")
            konfirmasi = input("Yakin untuk menghapus barang? (y/n): ")
            if konfirmasi.lower() == 'y':
                inventaris.pop(i)
                print("Barang berhasil dihapus dari inventaris.")
            else:
                print("Barang batal dihapus.")
            return
    print("Barang tidak ditemukan di dalam inventaris.")

def search():
    print("\n=== CARI BARANG ===")
    if len(inventaris) == 0:
        print("Belum ada barang di dalam inventaris.")
        return
    keyword = input("Masukkan nama barang : ").lower()    
    hasil = []
    for barang in inventaris:
        if keyword in barang['nama'].lower() or keyword in barang['kode'].lower():
            hasil.append(barang)
    if len(hasil) > 0:
        print(f"\nDitemukan {len(hasil)} barang:")
        for barang in hasil:
            print(f"\nKode: {barang['kode']}")
            print(f"Nama: {barang['nama']}")
            print(f"Kategori: {barang['kategori']}")
            print(f"Jumlah: {barang['jumlah']}")
            print(f"Lokasi: {barang['lokasi']}")
            print("-" * 30)
    else:
        print("Barang tidak ditemukan di inventaris.")

def sorting():
    print("\n=== URUTKAN BARANG ===")
    if len(inventaris) == 0:
        print("Belum ada barang di dalam inventaris.")
        return
    print("1. Urutkan berdasarkan Nama (A-Z)")
    print("2. Urutkan berdasarkan Jumlah (Terkecil-Terbesar)")
    pilihan = int(input("Pilih (1/2): "))
    if pilihan == 1:
        for i in range(len(inventaris)):
            for j in range(i+1, len(inventaris)):
                if inventaris[i]['nama'] > inventaris[j]['nama']:
                    temp = inventaris[i]
                    inventaris[i] = inventaris[j]
                    inventaris[j] = temp
        print("\nBarang sudah diurutkan berdasarkan nama:")
    elif pilihan == 2:
        for i in range(len(inventaris)):
            for j in range(i+1, len(inventaris)):
                if inventaris[i]['jumlah'] > inventaris[j]['jumlah']:
                    temp = inventaris[i]
                    inventaris[i] = inventaris[j]
                    inventaris[j] = temp
        print("\nBarang sudah diurutkan berdasarkan jumlah:")
    else:
        print("Pilihan tidak valid (1/2).")
        return
    for barang in inventaris:
        print(f"\n{barang['nama']} - Jumlah: {barang['jumlah']}")
print("=" * 40)
print("APLIKASI INVENTARIS BARANG KANTOR SOMAT")
print("=" * 40)

while True:
    print("\n--- MENU ---")
    print("1. Tambah Barang")
    print("2. Lihat Semua Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Urutkan Barang")
    print("7. Keluar")
    pilihan = input("\nPilih menu (1-7): ")  
    if pilihan == "1":
        create()
    elif pilihan == "2":
        read()
    elif pilihan == "3":
        update()
    elif pilihan == "4":
        delete()
    elif pilihan == "5":
        search()
    elif pilihan == "6":
        sorting()
    elif pilihan == "7":
        print("\nTerima kasih telah menggunakan aplikasi inventaris barang kantor Somat.")
        break
    else:
        print("Pilihan tidak valid (1-7).")