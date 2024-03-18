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
            HpGaming("IPhone 13 Pro Max", "A15 Bionic", "6", "256", "Silver", 15000000),
            HpGaming("Samsung Galaxy S21 Ultra", "Exynos 2100", "12", "256", "Black Galaxy", 18000000),
            HpGaming("Xiaomi Black Shark 4", "Snapdragon 870", "8", "128", "Black Green", 6000000),
            HpGaming("Infinix Note 30", "Snapdragon 888", "8", "256", "Green", 9000000),
        ]

class NodeHpGaming:
    def __init__(self, hp):
        self.hp = hp
        self.next = None

class LinkedHpGaming:
    def __init__(self, daftar_hp):
        self.head = None
        if isinstance(daftar_hp, DaftarHpGaming):
            for hp in daftar_hp.daftar_hp:
                self.tambah_hp_di_akhir(hp)

    def tampilkan_hp(self):
        current = self.head
        if not current:
            os.system("cls" if os.name == "nt" else "clear")
            print("Daftar HP Gaming Belum Tersedia...")
            return
        nomor = 1
        while current:
            hp = current.hp
            print(f"{nomor}. Nama: {hp.nama}, Processor: {hp.processor}, RAM: {hp.ram} GB, Storage: {hp.storage} GB, Warna: {hp.warna}, Harga: Rp. {hp.harga}")
            current = current.next
            nomor += 1

    def tambah_hp_di_awal(self, hp):
        new_node = NodeHpGaming(hp)
        new_node.next = self.head
        self.head = new_node

    def tambah_hp_di_antara(self, hp, posisi):
        new_node = NodeHpGaming(hp)
        if posisi == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(1, posisi-1):
            if current is None:
                print("Posisi melebihi jumlah HP.")
                return
            current = current.next
        if current is None:
            print("Posisi tidak valid.")
            return
        new_node.next = current.next
        current.next = new_node

    def tambah_hp_di_akhir(self, hp):
        new_node = NodeHpGaming(hp)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def hapus_hp_di_awal(self):
        if self.head is None:
            print("Daftar HP kosong.")
            return
        self.head = self.head.next

    def hapus_hp_di_antara(self, posisi):
        if self.head is None:
            print("Daftar HP kosong.")
            return
        if posisi == 1:
            self.head = self.head.next
            return
        current = self.head
        for i in range(posisi - 2):
            if current.next is None:
                print("Posisi tidak valid.")
                return
            current = current.next
        if current.next is None:
            print("Tidak ada HP di posisi tersebut.")
            return
        current.next = current.next.next

    def hapus_hp_di_akhir(self):
        if self.head is None:
            print("Daftar HP kosong.")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def update_hp(self, posisi, nama, processor, ram, storage, warna, harga):
        current = self.head
        for i in range(1, posisi):
            if current is None:
                print("Posisi melebihi jumlah HP.")
                return
            current = current.next
        if current is None:
            print("Posisi tidak valid.")
            return
        current.hp.nama = nama
        current.hp.processor = processor
        current.hp.ram = ram
        current.hp.storage = storage
        current.hp.warna = warna
        current.hp.harga = harga
        print("Data HP berhasil diupdate.")

    def merge_sort(self, head, attribute1, attribute2, ascending=True):
            if head is None or head.next is None:
                return head

            mid = self._get_middle(head)
            left = head
            right = mid.next
            mid.next = None

            left = self.merge_sort(left, attribute1, attribute2, ascending)
            right = self.merge_sort(right, attribute1, attribute2, ascending)

            sorted_list = self._merge(left, right, attribute1, attribute2, ascending)
            return sorted_list

    def _get_middle(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right, attribute1, attribute2, ascending=True):
        if left is None:
            return right
        if right is None:
            return left

        if (ascending and getattr(left.hp, attribute1) < getattr(right.hp, attribute1)) or \
            (not ascending and getattr(left.hp, attribute1) > getattr(right.hp, attribute1)):
            left.next = self._merge(left.next, right, attribute1, attribute2, ascending)
            return left
        else:
            right.next = self._merge(left, right.next, attribute1, attribute2, ascending)
            return right

    def sort_hp(self, attribute1, attribute2, ascending=True):
        self.head = self.merge_sort(self.head, attribute1, attribute2, ascending)

    def jump_search(self, key, by='nama'):
        current = self.head
        while current:
            if by == 'nama' and current.hp.nama.lower() == key.lower():
                return current.hp
            elif by == 'harga' and current.hp.harga == key:
                return current.hp
            current = current.next
        return None

def main():
    daftar_hp = DaftarHpGaming()
    linked_hp = LinkedHpGaming(daftar_hp)

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~  Welcome Rekomendasi HP Gaming ~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nPilih Menu di Bawah Ini :\n")
        print("1. Tampilkan HP Gaming")
        print("2. Tambah HP Gaming")
        print("3. Update HP Gaming")
        print("4. Hapus HP Gaming")
        print("5. Sortir HP Gaming")
        print("6. Cari HP Gaming")
        print("7. Keluar")

        pilihan = input("\nMasukkan pilihan yang anda inginkan: ")

        if pilihan == "1":
            os.system("cls")
            print("DAFTAR REKOMENDASI HP GAMING :")
            linked_hp.tampilkan_hp()
        elif pilihan == "2":
            nama = input("Nama HP: ")
            processor = input("Processor: ")
            ram = input("RAM (GB): ")
            storage = input("Storage (GB): ")
            warna = input("Warna: ")
            harga = int(input("Harga: "))
            hp = HpGaming(nama, processor, ram, storage, warna, harga)
            posisi = input("Tambah HP di posisi (1: awal, 2: antara, 3: akhir): ")
            if posisi == "1":
                linked_hp.tambah_hp_di_awal(hp)
            elif posisi == "2":
                posisi_tambahan = int(input("Masukkan Nomor Yang Di Inginkan: "))
                linked_hp.tambah_hp_di_antara(hp, posisi_tambahan)
            elif posisi == "3":
                linked_hp.tambah_hp_di_akhir(hp)
            else:
                print("Pilihan tidak valid.")
            print("HP Berhasil Di Tambahkan!")
        elif pilihan == "3":
            linked_hp.tampilkan_hp()
            posisi_update = int(input("\nMasukkan nomor HP yang ingin diupdate: "))
            nama = input("Nama HP baru: ")
            processor = input("Processor baru: ")
            ram = input("RAM baru (GB): ")
            storage = input("Storage baru (GB): ")
            warna = input("Warna baru: ")
            harga = int(input("Harga baru: "))
            linked_hp.update_hp(posisi_update, nama, processor, ram, storage, warna, harga)
        elif pilihan == "4":
            if linked_hp.head is not None:
                linked_hp.tampilkan_hp()
                posisi_hapus = int(input("\nMasukkan nomor HP yang ingin dihapus: "))
                if posisi_hapus == 1:
                    linked_hp.hapus_hp_di_awal()
                elif posisi_hapus == len(daftar_hp.daftar_hp):
                    linked_hp.hapus_hp_di_akhir()
                else:
                    linked_hp.hapus_hp_di_antara(posisi_hapus)
                print("HP Berhasil Di Hapus!")
            else:
                os.system("cls")
                print("Daftar HP Gaming Belum Tersedia...")
                input("\nTekan enter untuk kembali ke menu utama...")
        elif pilihan == "5":
            print("\nOpsi Sortir:\n")
            print("1. Sortir Ascending berdasarkan Harga")
            print("2. Sortir Descending berdasarkan Harga")
            print("3. Sortir Ascending berdasarkan Nama")
            print("4. Sortir Descending berdasarkan Nama")

            sort_option = input("\nMasukkan pilihan sortir: ")

            if sort_option == "1":
                linked_hp.sort_hp("harga", "nama", ascending=True)
                print("Daftar HP berhasil diurutkan secara ascending berdasarkan Harga.")
            elif sort_option == "2":
                linked_hp.sort_hp("harga", "nama", ascending=False)
                print("Daftar HP berhasil diurutkan secara descending berdasarkan Harga.")
            elif sort_option == "3":
                linked_hp.sort_hp("nama", "harga", ascending=True)
                print("Daftar HP berhasil diurutkan secara ascending berdasarkan Nama.")
            elif sort_option == "4":
                linked_hp.sort_hp("nama", "harga", ascending=False)
                print("Daftar HP berhasil diurutkan secara descending berdasarkan Nama.")
            else:
                print("Pilihan tidak valid.")
                input("\nTekan enter untuk kembali ke menu utama...")
        elif pilihan == "6":
            os.system("cls" if os.name == "nt" else "clear")
            print("Pilihan pencarian:")
            print("1. Cari berdasarkan nama")
            print("2. Cari berdasarkan harga")
            pilihan_cari = input("\nPilih jenis pencarian: ")
            if pilihan_cari == "1":
                nama_cari = input("Masukkan nama HP yang ingin dicari: ")
                hasil_nama = linked_hp.jump_search(nama_cari, by='nama')
                if hasil_nama:
                    print(f"\nHP dengan nama '{nama_cari}' ditemukan.")
                    print(f"Detail HP: {hasil_nama.nama}, Processor: {hasil_nama.processor}, Harga: {hasil_nama.harga}")
                else:
                    print(f"\nHP dengan nama '{nama_cari}' tidak ditemukan.")
            elif pilihan_cari == "2":
                harga_cari = int(input("Masukkan harga HP yang ingin dicari: "))
                hasil_harga = linked_hp.jump_search(harga_cari, by='harga')
                if hasil_harga:
                    print(f"\nHP dengan harga '{harga_cari}' ditemukan.")
                    print(f"Detail HP: {hasil_harga.nama}, Processor: {hasil_harga.processor}, Harga: {hasil_harga.harga}")
                else:
                    print(f"\nHP dengan harga '{harga_cari}' tidak ditemukan.")
            else:
                print("\nPilihan tidak valid.")
                input("\nTekan enter untuk kembali ke menu utama...")
        elif pilihan == "7":
            os.system("cls")
            print("Thank You For Using Recomendded Me!")
            break
        else:
            print("Pilihan tidak valid, silahkan masukkan pilihan yang benar...")
        input("\nTekan enter untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()
