def create(data):
    print("Tambah Produk JavaKulit")
    nama = input("Nama produk: ")

    try:
        stok = int(input("Stok produk: "))
        harga = int(input("Harga produk: "))
    except ValueError:
        print("Stok dan harga harus berupa angka!")
        return data

    data.append({
        "nama": nama,
        "stok": stok,
        "harga": harga,
    })

    print("Produk berhasil ditambahkan!")
    return data

def read(data):
    if len(data) == 0:
        print("Belum ada produk.")
        return

    print("Lihat Produk JavaKulit")
    print("1. Tampilkan semua produk")
    print("2. Cari produk")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Daftar Produk JavaKulit")
        for i in range(len(data)):
            d = data[i]
            print(i+1, ". ", d["nama"], " | Stok:", d["stok"], " | Harga: Rp", d["harga"])

    elif pilihan == "2":
        key = input("Masukkan kata kunci: ")
        print("Hasil Pencarian:")

        ketemu = False

        for i in range(len(data)):
            nama_produk = data[i]["nama"]

            if key in nama_produk:
                print(data[i]["nama"], "| Stok:", data[i]["stok"], "| Harga: Rp", data[i]["harga"])
                ketemu = True

        if ketemu == False:
            print("Produk tidak ditemukan.")

def update(data):
    if len(data) == 0:
        print("Belum ada produk.")
        return data

    print("Edit Produk JavaKulit")
    for i in range(len(data)):
        d = data[i]
        print(f"{i+1}. {d['nama']} | Stok: {d['stok']} | Harga: Rp {d['harga']}")

    try:
        index = int(input("Pilih nomor produk: ")) - 1
        if not (0 <= index < len(data)):
            print("Nomor tidak valid.")
            return data
    except ValueError:
        print("Input harus angka.")
        return data

    print("Apa yang ingin diubah?")
    print("1. Nama")
    print("2. Stok")
    print("3. Harga")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        data[index]["nama"] = input("Nama baru: ")

    elif pilihan == "2":
        try:
            data[index]["stok"] = int(input("Stok baru: "))
        except ValueError:
            print("Stok harus angka.")

    elif pilihan == "3":
        try:
            data[index]["harga"] = int(input("Harga baru: "))
        except ValueError:
            print("Harga harus angka.")

    else:
        print("Pilihan tidak valid.")
        return data

    print("Produk berhasil diupdate.")
    return data


def delete(data):
    if len(data) == 0:
        print("Belum ada produk.")
        return data

    print("Hapus Produk JavaKulit")
    for i in range(len(data)):
        d = data[i]
        print(f"{i+1}. {d['nama']} | Stok: {d['stok']} | Harga: Rp {d['harga']}")

    try:
        index = int(input("\nPilih nomor produk: ")) - 1
        if not (0 <= index < len(data)):
            print("Nomor tidak valid.")
            return data
    except ValueError:
        print("Input harus angka.")
        return data

    print(f"Produk '{data[index]['nama']}' telah dihapus.")
    del data[index]

    return data

def urutan_produk(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j]["harga"] > data[j + 1]["harga"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print("Produk berhasil diurutkan berdasarkan harga (termurah → termahal).")
    return data

def sorting(data):
    if len(data) == 0:
        print("Belum ada produk untuk diurutkan.")
        return data

    print("Sorting Produk")
    data = urutan_produk(data)
    read(data)
    input("Tekan ENTER untuk kembali...")
    return data

def menuUtama():
    print("===================================")
    print("===   Sistem Toko JavaKulit     ===")
    print("===================================")
    print("1. Tambah Produk")
    print("2. Lihat Produk")
    print("3. Edit Produk")
    print("4. Hapus Produk")
    print("5. Keluar")
    print("6. Mengurutkan produk berdasarkan harga")  

    try:
        pilihan = int(input("Masukkan pilihan [1 - 6]: "))
        if pilihan < 1 or pilihan > 6:
            print("Pilihan hanya 1 - 6!")
            return 0
        return pilihan

    except ValueError:
        print("Input harus angka.")
        return 0

data = []
pilihan = 0

while pilihan != 5:
    pilihan = menuUtama()

    if pilihan == 1:
        data = create(data)

    elif pilihan == 2:
        read(data)
        input("Tekan ENTER untuk kembali...")

    elif pilihan == 3:
        data = update(data)

    elif pilihan == 4:
        data = delete(data)

    elif pilihan == 6:
        data = sorting(data)

print("Terima kasih telah menggunakan JavaKulit!")