def bubble_sort(data):
    n = len(data)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]['judul'].lower() > data[j + 1]['judul'].lower():
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def create(data):
    print("\n=== Tambah Buku ===")
    judul = input("Masukkan Judul Buku   : ")
    penulis = input("Masukkan Nama Penulis : ")
    tahun = input("Masukkan Tahun Terbit : ")





    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun
    }

    data.append(buku)
    print("Buku berhasil ditambahkan!\n")
    return data


def read(data):
    print("\n=== Lihat Buku ===")

    if len(data) == 0:
        print("Belum ada buku yang tersimpan.\n")
        return

    print("1. Tampilkan semua buku (sorted berdasarkan judul, Bubble Sort)")
    print("2. Cari buku berdasarkan judul")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        print("\n--- Semua Buku (Bubble Sort) ---")

        
        data_sorted = data.copy()

        
        bubble_sort(data_sorted)

        i = 0
        while i < len(data_sorted):
            buku = data_sorted[i]
            print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
            i += 1

    elif pilihan == "2":
        keyword = input("Masukkan judul buku yang dicari: ") 
        print("\n--- Hasil Pencarian ---")

        ditemukan = False
        i = 0
        while i < len(data):
            buku = data[i]
            if keyword.lower() in buku["judul"].lower():
                print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
                ditemukan = True
            i += 1

        if not ditemukan:
            print("Buku tidak ditemukan.")


    print()


def update(data):
    print("\n=== Update Buku ===")

    if len(data) == 0:
        print("Belum ada buku.\n")
        return data

    i = 0
    while i < len(data):
        buku = data[i]
        print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
        i += 1

    try:
        index = int(input("Pilih nomor buku yang ingin diupdate: ")) - 1
        if index < 0 or index >= len(data):
            print("Nomor tidak valid.\n")
            return data
    except ValueError:
        print("Input harus angka.\n")
        return data

    print("\nMasukkan data baru (biarkan kosong jika tidak ingin mengubah):")
    judul_baru = input("Judul baru   : ")
    penulis_baru = input("Penulis baru : ")
    tahun_baru   = input("Tahun baru   : ")

    if judul_baru != "":
        data[index]["judul"] = judul_baru
    if penulis_baru != "":
        data[index]["penulis"] = penulis_baru
    if tahun_baru != "":
        data[index]["tahun"] = tahun_baru

    print("Data buku berhasil diperbarui!\n")
    return data


def delete(data):
    print("\n=== Hapus Buku ===")

    if len(data) == 0:
        print("Belum ada buku.\n")
        return data

    i = 0
    while i < len(data):
        buku = data[i]
        print(f"{i+1}. {buku['judul']} - {buku['penulis']} ({buku['tahun']})")
        i += 1

    try:
        index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(data):
            print("Nomor tidak valid.\n")
            return data
    except ValueError:
        print("Input harus angka.\n")
        return data

    konfirmasi = input(f"Yakin ingin menghapus '{data[index]['judul']}'? (y/n): ")
    if konfirmasi.lower() == "y":
        data.pop(index)
        print("Buku berhasil dihapus!\n")
    else:
        print("Buku tidak dihapus.\n")

    return data


def menuUtama():
    print("===================================")
    print("===     Data Buku Perpustakaan   ===")
    print("===    by Perpustakaan Balikpapan  ===")
    print("===================================")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Edit Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya 1 sampai 5.")
            input()
        else:
            return pilihan
    except ValueError:
        print("Input harus angka.")




pilihan = 0
data = []

while pilihan != 5:
    pilihan = menuUtama()

    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
        input("Kembali tekan ENTER..")
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)

print("Terima kasih..!")