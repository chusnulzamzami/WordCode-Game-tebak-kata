import random

# Kelas utama untuk permainan WordCode
class WordCodeGame:
    # Inisialisasi permainan dengan nama pemain dan kategori yang dipilih
    def __init__(self, nama_pemain, kategori):
        self.nama_pemain = nama_pemain  # Nama pemain
        self.kategori = kategori  # Kategori yang dipilih pemain
        # Daftar kata berdasarkan kategori
        self.kata_kategori = {
            "hewan": ["gajah", "singa", "kucing", "burung", "ikan", "kelinci", "harimau", "kalajengking"],
            "buah-buahan": ["apel", "pisang", "jeruk", "mangga", "melon", "semangka", "durian", "anggur"],
            "nama dosen": ["mahyus", "husaini", "arie", "kikye", "rasudin", "zulfan", "muslim"],
            "nama jurusan di MIPA": ["matematika", "fisika", "kimia", "biologi", "statistika", "informatika", "manajemeninformatika", "farmasi"]
        }
        # Memilih kata secara acak dari kategori yang dipilih
        self.kata = random.choice(self.kata_kategori[kategori])
        self.tebakan_huruf = []  # Daftar huruf yang sudah ditebak
        self.kesempatan = 5  # Nyawa pemain (jumlah kesempatan menebak)
        self.skor = 100  # Skor awal adalah 100, berkurang dengan setiap kesalahan

    # Menampilkan status permainan, yaitu kata yang sudah ditebak dan nyawa tersisa
    def tampilkan_status(self):
        # Tampilkan huruf yang benar dan tanda '_' untuk huruf yang belum ditebak
        status = ''.join([huruf if huruf in self.tebakan_huruf else '_' for huruf in self.kata])
        print(f"\nKata: {status}")
        print(f"Nyawa anda tersisa: {self.kesempatan}")

    # Metode untuk menebak huruf
    def tebak_huruf(self, huruf):
        # Jika huruf sudah pernah ditebak
        if huruf in self.tebakan_huruf:
            print("Anda sudah menebak huruf ini. Coba huruf lain.")
        # Jika huruf ada dalam kata, tambahkan ke daftar tebakan_huruf
        elif huruf in self.kata:
            self.tebakan_huruf.append(huruf)
            print(f"Bagus! Huruf '{huruf}' ada dalam kata.")
        # Jika huruf tidak ada dalam kata, kurangi nyawa dan skor
        else:
            self.tebakan_huruf.append(huruf)
            self.kesempatan -= 1
            self.skor -= 20  # Kurangi skor sebesar 20 poin
            print(f"Sayang sekali! Huruf '{huruf}' tidak ada dalam kata.")

    # Cek apakah pemain sudah berhasil menebak seluruh huruf dalam kata
    def sudah_menang(self):
        return all(huruf in self.tebakan_huruf for huruf in self.kata)

    # Metode utama yang menjalankan permainan
    def main_game(self):
        print(f"\nHaloo {self.nama_pemain}, Anda memilih Level: {self.kategori} \nSelamat bermain dan semoga berhasil:)")
        # Looping selama pemain belum menang dan masih ada nyawa
        while not self.sudah_menang() and self.kesempatan > 0:
            self.tampilkan_status()
            tebakan = input("Tebak huruf: ").lower()  # Input huruf tebakan
            self.tebak_huruf(tebakan)

        # Setelah permainan berakhir, tampilkan hasil dan skor akhir
        if self.sudah_menang():
            print(f"\nSelamat {self.nama_pemain} Anda berhasil menebak kata: {self.kata}")
        else:
            print(f"\nSayang sekali {self.nama_pemain} Anda kehabisan kesempatan:( Kata yang benar adalah: {self.kata}")
        
        print(f"Skor akhir Anda adalah: {self.skor}")

# Kelas untuk informasi tambahan permainan
class Game:
    # Deskripsi singkat tentang permainan
    @staticmethod
    def deskripsi_game():
        print("\n=== Deskripsi Permainan ===")
        print("WordCode adalah permainan tebak kata di mana pemain harus menebak huruf-huruf dalam kata yang tersembunyi.")
        print("Pemain memiliki 5 nyawa untuk menebak huruf. Jika pemain salah menebak, nyawa pemain akan berkurang.")
        print("Tujuannya adalah untuk menebak kata sebelum kehabisan nyawa.")
        print("Selamat bermain dan semoga beruntung!")

    # Petunjuk dan tata cara bermain
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

# Fungsi untuk memilih kategori permainan
def pilih_kategori():
    print("\n=== Pilih Level ===")
    print("1. Hewan")
    print("2. Buah-buahan")
    print("3. Nama dosen")
    print("4. Nama jurusan di MIPA")
    pilihan = input("Pilih kategori (1/2/3/4): ")
    # Mengembalikan nama kategori berdasarkan pilihan pengguna
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

# Fungsi menu utama permainan
def main_menu():
    print("=== Menu Utama ===")
    nama_pemain = input("Masukkan nama Anda: ")  # Input nama pemain
    print(f"\nSelamat datang di permainan WordCode, {nama_pemain}! Silahkan pilih menu bagian bawah ini untuk memulai permainan.")
    # Looping menu utama
    while True:
        print("\n1. Mulai Permainan")
        print("2. Deskripsi Permainan")
        print("3. Tata Cara bermain")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ")

        # Menjalankan fungsi sesuai pilihan pemain
        if pilihan == '1':
            kategori = pilih_kategori()
            game = WordCodeGame(nama_pemain, kategori)  # Membuat objek permainan
            game.main_game()  # Memulai permainan
        elif pilihan == '2':
            Game.deskripsi_game()  # Menampilkan deskripsi permainan
        elif pilihan == '3':
            Game.tata_cara_permainan()  # Menampilkan tata cara permainan
        elif pilihan == '4':
            print(f"Terima kasih {nama_pemain} telah bermain! Sampai jumpa!")  # Keluar dari permainan
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Memulai program dengan memanggil main_menu
if __name__ == "__main__":
    main_menu() 
