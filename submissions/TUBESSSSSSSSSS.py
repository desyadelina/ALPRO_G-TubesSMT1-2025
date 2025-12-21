produk_petshop = [
    ["whiskas", 0, 15000, 0, "Tersedia", 10],
    ["royal canin", 0, 25000, 0, "Tersedia", 8],
    ["pasir", 0, 12000, 0, "Tersedia", 12],
    ["shampo kucing", 0, 8000,  0, "Tersedia", 7],
    ["obat", 0, 45000, 0, "Tersedia", 5]]

def create(data):
    print("\n=== Tambah Data Pembelian ===")
    print("Daftar Produk:")

    for i in range(len(data)):
        print(str(i + 1) + ". " + data[i][0] + " - Stok: " + str(data[i][5]))

    try:
        pilihan = int(input("Pilih produk (1-5): ").strip())
    except:
        print("Input harus angka.")
        return data

    if pilihan < 1 or pilihan > 5:
        print("Pilihan produk tidak ada.")
        return data

    produk = data[pilihan - 1]

    if produk[5] <= 0:
        print("Stok habis.")
        return data

    try:
        jumlah = int(input("Jumlah dibeli: ").strip())
    except:
        print("Jumlah harus angka.")
        return data

    if jumlah <= 0:
        print("Jumlah minimal 1.")
        return data

    if jumlah > produk[5]:
        print("Stok tidak cukup. Stok tersedia:", produk[5])
        return data

    total_bayar = jumlah * produk[2]

    produk[1] = produk[1] + jumlah
    produk[3] = produk[3] + total_bayar
    produk[5] = produk[5] - jumlah
    produk[4] = "Terjual"

    print(produk[0] + " berhasil dijual. Total bayar: Rp" + str(total_bayar))
    print("Sisa stok:", produk[5])

    return data

def read(data):
    print("\n=== DATA PRODUK PETSHOP ===")
    print("Produk | Terjual | Harga | Pendapatan | Status | Stok")

    for p in data:
        print(
            p[0] + " | " +
            str(p[1]) + " pcs | " +
            "Rp" + str(p[2]) + " | " +
            "Rp" + str(p[3]) + " | " +
            p[4] + " | " +
            str(p[5])
        )

def update(data):
    print("\n=== Update Stok Produk ===")
    read(data)

    try:
        pilihan = int(input("Pilih produk (1-5): ").strip())
    except:
        print("Input harus angka.")
        return data

    if pilihan < 1 or pilihan > 5:
        print("Produk tidak ada.")
        return data

    produk = data[pilihan - 1]

    print("Stok sekarang:", produk[5])

    try:
        tambah = int(input("Tambah stok berapa: ").strip())
    except:
        print("Stok harus angka.")
        return data

    if tambah < 0:
        print("Tidak boleh negatif.")
        return data

    produk[5] = produk[5] + tambah
    print("Stok untuk " + produk[0] + " sekarang menjadi " + str(produk[5]))

    return data

def sort_stok(data):
    print("\n=== Sorting Berdasarkan Stok ===")

    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][5] > data[j + 1][5]: 
                data[j], data[j + 1] = data[j + 1], data[j]

    read(data)
    return data

def search(data):
    print("\n=== Pencarian Produk ===")
    nama = input("Masukkan nama produk: ").strip().lower()

    ditemukan = False
    for p in data:
        if nama in p[0].lower():
            print("\nProduk ditemukan:")
            print(
                p[0] + " | Terjual: " + str(p[1]) +
                " | Harga: Rp" + str(p[2]) +
                " | Pendapatan: Rp" + str(p[3]) +
                " | Status: " + p[4] +
                " | Stok: " + str(p[5])
            )
            ditemukan = True

    if not ditemukan:
        print("Produk tidak ditemukan.")

    return data

def delete(data):
    print("\n=== RESET SEMUA DATA ===")
    yakin = input("Yakin reset semua data? (y/n): ").lower().strip()

    if yakin == "y":
        for p in data:
            p[1] = 0
            p[3] = 0
            p[4] = "Tersedia"
            p[5] = 10
        print("Semua data telah direset.")

    return data

def menu():
    print("\n===============================")
    print("     PETSHOP NINGNING ")
    print("===============================")
    print("1. Tambah Pembelian")
    print("2. Lihat Data")
    print("3. Update Stok Produk")
    print("4. Sorting & Searching")
    print("5. Reset Data & Keluar")

    try:
        return int(input("Pilih menu (1-5): ").strip())
    except:
        return 0

def main():
    pilihan = 0

    while pilihan != 5:
        pilihan = menu()

        if pilihan == 1:
            create(produk_petshop)
        elif pilihan == 2:
            read(produk_petshop)
        elif pilihan == 3:
            update(produk_petshop)
        elif pilihan == 4:
            print("\n1. Sorting Stok\n2. Searching Produk")
            sub = input("Pilih (1/2): ").strip()
            if sub == "1":
                sort_stok(produk_petshop)
            elif sub == "2":
                search(produk_petshop)
        elif pilihan == 5:
            delete(produk_petshop)
            print("Program selesai.")
        else:
            print("Menu tidak valid.")


main()