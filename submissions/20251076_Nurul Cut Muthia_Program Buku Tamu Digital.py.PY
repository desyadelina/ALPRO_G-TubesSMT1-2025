# PROGRAM BUKU TAMU DIGITAL

def create(data):
    print("\n=== TAMBAH DATA TAMU ===")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    keperluan = input("Keperluan: ")
    
    if not data:
        id_tamu = "1001"
    else:
        last_id = data[-1][0]
        last_num = int(last_id[1:])
        id_tamu = f"T{last_num + 1:03d}"
    
    from datetime import datetime
    tanggal = datetime.now().strftime("%d/%m/%Y")
    
    data.append([id_tamu, nama, alamat, keperluan, tanggal])
    print(f"Data {id_tamu} ditambah")
    return data

def read(data):
    print("\n=== DAFTAR ID DAN NAMA TAMU ===")
    if not data:
        print("Kosong")
        return
    
    for item in data:
        print(f"{item[0]} - {item[1]} - {item[4]}")

def update(data):
    print("\n=== EDIT DATA TAMU ===")
    if not data:
        print("Kosong")
        return data
    
    id_cari = input("ID tamu: ")
    for i in range(len(data)):
        if data[i][0] == id_cari:
            nama = input(f"Nama [{data[i][1]}]: ") or data[i][1]
            alamat = input(f"Alamat [{data[i][2]}]: ") or data[i][2]
            keperluan = input(f"Keperluan [{data[i][3]}]: ") or data[i][3]
            
            data[i][1] = nama
            data[i][2] = alamat
            data[i][3] = keperluan
            print("Berhasil update")
            return data
    
    print("Tidak ditemukan")
    return data

def delete(data):
    print("\n=== HAPUS DATA TAMU ===")
    if not data:
        print("Kosong")
        return data
    
    id_hapus = input("ID tamu: ")
    for i in range(len(data)):
        if data[i][0] == id_hapus:
            data.pop(i)
            print("Terhapus")
            return data
    
    print("Tidak ditemukan")
    return data

def menuUtama():
    print("\n=== BUKU TAMU DIGITAL ===")
    print("1. Tambah Data Tamu")
    print("2. Lihat Jumlah Tamu")
    print("3. Edit Data Tamu")
    print("4. Hapus Data Tamu")
    print("5. Keluar")
    
    try:
        pilih = int(input("Pilih [1-5]: "))
        return pilih
    except:
        return 0

# PROGRAM UTAMA
pilihan = 0
data = []

while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)

print("Selesai")