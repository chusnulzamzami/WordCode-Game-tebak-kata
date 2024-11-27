import random
import json  # Untuk menyimpan dan memuat data skor ke file


# Kelas utama untuk permainan WordCode
class WordCodeGame:
    def __init__(self, nama_pemain, kategori, level):
        self.nama_pemain = nama_pemain
        self.kategori = kategori
        self.level = level
        self.kata_kategori = {
            "hewan": ["gajah", "singa", "kucing", "burung", "ikan", "kelinci", "harimau", "kalajengking", "kapibara", "rubah", "sapi", "kerbau", "trenggiling", "ayam", "beruang", "jerapah", "kuda", "badak", "buaya"],
            "buah-buahan": ["apel", "pisang", "jeruk", "mangga", "melon", "semangka", "durian", "anggur", "belimbing", "pepaya", "alpukat", "jambu", "kelengkeng", "nanas", "strawberry", "leci", "kiwi"],
            "nama dosen": ["mahyus", "husaini", "arie", "kikye", "rasudin", "zulfan", "muslim", "marzuki", "sri", "razief"],
            "nama jurusan di MIPA": ["matematika", "fisika", "kimia", "biologi", "statistika", "informatika", "manajemeninformatika", "farmasi"]
        }
        self.kata = self.pilih_kata_level()
        self.tebakan_huruf = []
        self.kesempatan = 5
        self.skor = 100
        self.bantuan_digunakan = False

    def pilih_kata_level(self):
        if self.level == 'mudah':
            return random.choice(self.kata_kategori[self.kategori])
        elif self.level == 'medium':
            return ' '.join(random.choices(self.kata_kategori[self.kategori], k=2))
        elif self.level == 'sulit':
            return ' '.join(random.choices(self.kata_kategori[self.kategori], k=3))

    def tampilkan_status(self):
        status = ''.join([huruf if huruf in self.tebakan_huruf or huruf == ' ' else '_' for huruf in self.kata])
        print(f"\nKata: {status}")
        print(f"Nyawa anda tersisa: {self.kesempatan}")

    def tebak_huruf(self, huruf):
        if huruf in self.tebakan_huruf:
            print("Anda sudah menebak huruf ini. Coba huruf lain.")
        elif huruf in self.kata:
            self.tebakan_huruf.append(huruf)
            print(f"Bagus! Huruf '{huruf}' ada dalam kata.")
        else:
            self.tebakan_huruf.append(huruf)
            self.kesempatan -= 1
            self.skor -= 20
            print(f"Sayang sekali! Huruf '{huruf}' tidak ada dalam kata.")

    def sudah_menang(self):
        return all(huruf in self.tebakan_huruf or huruf == ' ' for huruf in self.kata)

    def gunakan_bantuan(self):
        if self.bantuan_digunakan:
            print("Anda sudah menggunakan bantuan sebelumnya.")
        else:
            self.bantuan_digunakan = True
            for huruf in self.kata:
                if huruf not in self.tebakan_huruf and huruf != ' ':
                    self.tebakan_huruf.append(huruf)
                    print(f"Bantuan: Huruf '{huruf}' telah diungkapkan!")
                    break

    def main_game(self):
        print(f"\nHalo {self.nama_pemain}, Anda memilih Level: {self.level.capitalize()} - Kategori: {self.kategori.capitalize()} \nSelamat bermain dan semoga berhasil :)")
        while not self.sudah_menang() and self.kesempatan > 0:
            self.tampilkan_status()
            tebakan = input("Tebak huruf (atau ketik 'bantuan' untuk bantuan): ").lower()

            if tebakan == "bantuan":
                self.gunakan_bantuan()
            else:
                self.tebak_huruf(tebakan)

        if self.sudah_menang():
            print(f"\nSelamat {self.nama_pemain}, Anda berhasil menebak kata: {self.kata}")
        else:
            print(f"\nSayang sekali {self.nama_pemain}, Anda kehabisan kesempatan :( Kata yang benar adalah: {self.kata}")

        print(f"Skor akhir Anda adalah: {self.skor}")
        return self.skor


class Game:
    skor_board = {}

    @staticmethod
    def deskripsi_game():
        print("\n=== Deskripsi Permainan ===")
        print("WordCode adalah permainan tebak kata di mana pemain harus menebak huruf-huruf dalam kata yang tersembunyi.")
        print("Pemain memiliki 5 nyawa untuk menebak huruf. Jika pemain salah menebak, nyawa pemain akan berkurang.")
        print("Tujuannya adalah untuk menebak kata sebelum kehabisan nyawa.")
        print("Pilih tingkat kesulitan: Mudah (1 kata), Medium (2 kata), atau Sulit (3 kata).")
        print("Gunakan bantuan untuk mendapatkan petunjuk jika perlu.")
        print("Selamat bermain dan semoga beruntung!")

    @staticmethod
    def tata_cara_permainan():
        print("\n=== Tata Cara Permainan ===")
        print("1. Pemain akan diberikan kata yang tersembunyi, yang ditunjukkan dengan garis bawah (_).")
        print("2. Pemain harus menebak huruf satu per satu.")
        print("3. Jika huruf yang ditebak ada dalam kata, huruf tersebut akan ditampilkan.")
        print("4. Jika huruf tidak ada dalam kata, nyawa pemain akan berkurang.")
        print("5. Pemain memiliki 5 nyawa untuk menebak huruf.")
        print("6. Skor awal adalah 100. Setiap kesalahan mengurangi 20 poin dari skor.")
        print("7. Permainan berakhir ketika pemain berhasil menebak kata atau kehabisan nyawa.")


    @staticmethod
    def tampilkan_skor_board():
        print("\n=== Skor Board ===")
        if not Game.skor_board:
            print("Belum ada pemain yang mencatatkan skor.")
        else:
            # Urutkan pemain berdasarkan skor tertinggi
            sorted_board = sorted(Game.skor_board.items(), key=lambda x: max(x[1]), reverse=True)
            print("Daftar pemain dan skor:")
            for nama, daftar_skor in sorted_board:
                skor_str = ', '.join(map(str, sorted(daftar_skor, reverse=True)))
                print(f"{nama}: {skor_str} poin")

    @staticmethod
    def simpan_skor_ke_file():
        with open("skor_board.json", "w") as file:
            json.dump(Game.skor_board, file)
        print("Data skor telah disimpan.")

    @staticmethod
    def muat_skor_dari_file():
        try:
            with open("skor_board.json", "r") as file:
                Game.skor_board = json.load(file)
                
        except FileNotFoundError:
            print("File skor tidak ditemukan, memulai permainan dengan skor kosong.")


def pilih_kategori():
    print("\n=== Pilih Kategori ===")
    print("1. Hewan")
    print("2. Buah-buahan")
    print("3. Nama dosen")
    print("4. Nama jurusan di MIPA")
    pilihan = input("Pilih kategori (1/2/3/4): ")
    if pilihan == '1':
        return "hewan"
    elif pilihan == '2':
        return "buah-buahan"
    elif pilihan == '3':
        return "nama dosen"
    elif pilihan == '4':
        return "nama jurusan di MIPA"
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
        return pilih_kategori()


def pilih_level():
    print("\n=== Pilih Level ===")
    print("1. Mudah (1 kata)")
    print("2. Medium (2 kata)")
    print("3. Sulit (3 kata)")
    level = input("Pilih level (1/2/3): ")
    if level == '1':
        return 'mudah'
    elif level == '2':
        return 'medium'
    elif level == '3':
        return 'sulit'
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
        return pilih_level()


def main_menu():
    Game.muat_skor_dari_file()  # Muat skor dari file saat permainan dimulai
    print("=== Menu Utama ===")
    nama_pemain = input("Masukkan nama Anda: ")
    while True:
        print("\n1. Mulai Permainan")
        print("2. Deskripsi Permainan")
        print("3. Tata Cara Bermain")
        print("4. Tampilkan Skor Board")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == '1':
            kategori = pilih_kategori()
            level = pilih_level()
            game = WordCodeGame(nama_pemain, kategori, level)
            skor = game.main_game()
            # Simpan skor ke skor_board
            if nama_pemain in Game.skor_board:
                Game.skor_board[nama_pemain].append(skor)
            else:
                Game.skor_board[nama_pemain] = [skor]
        elif pilihan == '2':
            Game.deskripsi_game()
        elif pilihan == '3':
            Game.tata_cara_permainan()
        elif pilihan == '4':
            Game.tampilkan_skor_board()
        elif pilihan == '5':
            Game.simpan_skor_ke_file()
            print("Terima kasih telah bermain. Sampai jumpa lagi!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")


# Jalankan permainan
if __name__ == "__main__":
    main_menu()

