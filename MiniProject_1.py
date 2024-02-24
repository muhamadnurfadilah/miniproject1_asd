import os

class HpGaming:
    def __init__(self, nama, processor, ram, storage, warna, harga):
        self.nama = nama
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.warna = warna
        self.harga = harga

class DaftarHpGaming:
    def __init__(self):
        self.daftar_hp = [
            HpGaming("ROG Phone 5", "Snapdragon 888", "8", "256", "Black Red", 8000000),
            HpGaming("iPhone 13 Pro Max", "A15 Bionic", "6", "256", "Silver", 15000000),
            HpGaming("Samsung Galaxy S21 Ultra", "Exynos 2100", "12", "256", "Black Galaxy", 18000000),
            HpGaming("Xiaomi Black Shark 4", "Snapdragon 870", "8", "128", "Black Green", 6000000),
            HpGaming("Infinix Note 30", "Snapdragon 888", "8", "256", "Green", 9000000),
        ]

    def tampilkan_hp(self):
        for i, hp in enumerate(self.daftar_hp, start=1):
            print(f"{i}. Nama: {hp.nama}, Processor: {hp.processor}, RAM: {hp.ram} GB, Storage: {hp.storage} GB, Warna: {hp.warna}, Harga: Rp. {hp.harga}")

    def tambah_hp(self, nama, processor, ram, storage, warna, harga):
        self.daftar_hp.append(HpGaming(nama, processor, ram, storage, warna, harga))
        print("HP Gaming berhasil ditambahkan!")

    def update_hp(self, i, nama, processor, ram, storage, warna, harga):
        if 0 <= i < len(self.daftar_hp):
            self.daftar_hp[i] = HpGaming(nama, processor, ram, storage, warna, harga)
            print("Data HP Gaming berhasil diupdate!")
        else:
            print("Input Nomor Tidak Valid!")

    def hapus_hp(self, i):
        if 0 <= i < len(self.daftar_hp):
            del self.daftar_hp[i]
            print("HP Gaming berhasil dihapus!")
        else:
            print("Input Nomor Tidak Valid!")

# Membuat Variabel daftar_hp_gaming sebagai akses pemanggilan variabel untuk Menampilkan Class DaftarHpGaming()
daftar_hp_gaming = DaftarHpGaming()

#Main Program
while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~  Welcome Rekomendasi HP Gaming ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nPilih Menu di Bawah Ini :\n")
    print("1. Tambah HP Gaming")
    print("2. Tampilkan HP Gaming")
    print("3. Update HP Gaming")
    print("4. Hapus HP Gaming")
    print("5. Keluar")

    pilihan = input("\nMasukkan pilihan yang anda inginkan: ")

    if pilihan == '1':
        os.system("cls")
        nama = input("Nama HP Gaming: ")
        processor = input("Processor: ")
        ram = input("RAM: ")
        storage = input("Storage : ")
        warna = input("Warna: ")
        harga = input("Harga: ")
        daftar_hp_gaming.tambah_hp(nama, processor, ram, storage, warna, harga)
    elif pilihan == '2':
        os.system("cls")
        print("DAFTAR REKOMENDASI HP GAMING :")
        daftar_hp_gaming.tampilkan_hp()
    elif pilihan == '3':
        os.system("cls")
        daftar_hp_gaming.tampilkan_hp()
        i = int(input("\nMasukkan nomor HP Gaming yang ingin diupdate: ")) - 1
        nama = input("Nama baru: ")
        processor = input("Processor baru: ")
        ram = input("RAM baru (GB): ")
        storage = input("Storage baru (GB): ")
        warna = input("Warna baru: ")
        harga = input("Harga baru: ")
        daftar_hp_gaming.update_hp(i, nama, processor, ram, storage, warna, harga)
    elif pilihan == '4':
        os.system("cls")
        daftar_hp_gaming.tampilkan_hp()
        i = int(input("\nMasukkan nomor HP Gaming yang ingin dihapus: ")) - 1
        daftar_hp_gaming.hapus_hp(i)
    elif pilihan == '5':
        os.system("cls")
        print("Thank You For Using Recomendded Me!")
        break
    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk melanjutkan/kembali = ")

