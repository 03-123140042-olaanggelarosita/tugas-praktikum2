import random  

class Robot:
    def __init__(self, name, hp, attack, accuracy=0.8):
        """
        Konstruktor untuk kelas Robot.
        Menyimpan nama robot, HP, kekuatan serangan, dan akurasi serangan.
        """
        self.name = name  # Nama robot
        self.hp = hp  # Hitpoint robot (jumlah HP)
        self.attack = attack  # Kekuatan serangan robot
        self.accuracy = accuracy  # Akurasi serangan robot (kemungkinan serangan mengenai musuh)
    
    def attack_enemy(self, enemy_robot):
        """Melakukan serangan terhadap robot musuh, dengan kemungkinan miss (serangan meleset)."""
        # Menghasilkan angka acak antara 0 dan 1, jika lebih kecil dari akurasi maka serangan berhasil
        if random.random() <= self.accuracy:
            damage = self.attack  # Damage yang diberikan adalah kekuatan serangan robot
            enemy_robot.hp -= damage  # Mengurangi HP musuh sesuai dengan damage yang diterima
            print(f"{self.name} menyerang {enemy_robot.name} dan memberikan damage {damage}.")
        else:
            print(f"{self.name} gagal menyerang {enemy_robot.name}. Serangan meleset!")  # Pesan jika serangan gagal
    
    def regen_health(self):
        """Fungsi untuk regenerasi HP, tidak digunakan di sini, tapi bisa ditambahkan jika diperlukan."""
        # Ini bisa digunakan jika ada mekanisme penyembuhan HP untuk robot dalam game
        pass
    
    def is_alive(self):
        """Memeriksa apakah robot masih hidup (HP lebih besar dari 0)."""
        return self.hp > 0  # Mengembalikan True jika HP lebih dari 0, False jika HP 0 atau kurang

class Game:
    def __init__(self, robot1, robot2):
        """
        Konstruktor untuk kelas Game.
        Menyimpan dua robot yang akan bertarung dan ronde pertama dimulai.
        """
        self.robot1 = robot1  # Menyimpan robot pertama
        self.robot2 = robot2  # Menyimpan robot kedua
        self.round = 1  # Inisialisasi ronde pertama
    
    def print_status(self):
        """Mencetak status HP kedua robot setiap ronde."""
        # Menampilkan status kedua robot di setiap ronde
        print(f"Round-{self.round} ==========================================================")
        print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack}]")  # Status robot 1
        print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack}]\n")  # Status robot 2

    def player_action(self, robot):
        """Membuat pemain memilih aksi untuk robot mereka."""
        # Menampilkan opsi aksi yang tersedia untuk robot
        print(f"1. Attack 2. Defense 3. Giveup")
        action = input(f"{robot.name}, pilih aksi: ")  # Menerima input dari pemain untuk memilih aksi
        return action  # Mengembalikan aksi yang dipilih pemain

    def start(self):
        """Memulai permainan dan mengatur jalannya permainan hingga salah satu robot menang atau menyerah."""
        print(f"Permainan dimulai antara {self.robot1.name} dan {self.robot2.name}!\n")
        
        while self.robot1.is_alive() and self.robot2.is_alive():  # Selama kedua robot masih hidup
            self.print_status()  # Menampilkan status kedua robot setiap ronde

            # Robot 1 memilih aksi
            action1 = self.player_action(self.robot1)  # Pemain memilih aksi untuk robot 1
            if action1 == '1':  # Jika aksi 1 (Attack), maka robot 1 menyerang robot 2
                self.robot1.attack_enemy(self.robot2)
            elif action1 == '2':  # Jika aksi 2 (Defense), robot 1 memilih untuk bertahan
                print(f"{self.robot1.name} memilih untuk bertahan.")
            elif action1 == '3':  # Jika aksi 3 (Giveup), robot 1 menyerah
                print(f"{self.robot1.name} menyerah!")
                print(f"{self.robot2.name} menang!")
                return  # Mengakhiri permainan, karena robot 1 menyerah
            
            # Cek apakah robot 2 masih hidup setelah serangan
            if not self.robot2.is_alive():  # Jika robot 2 sudah mati (HP <= 0)
                print(f"{self.robot1.name} menang!")  # Robot 1 menang
                return
            
            # Robot 2 memilih aksi
            action2 = self.player_action(self.robot2)  # Pemain memilih aksi untuk robot 2
            if action2 == '1':  # Jika aksi 1 (Attack), maka robot 2 menyerang robot 1
                self.robot2.attack_enemy(self.robot1)
            elif action2 == '2':  # Jika aksi 2 (Defense), robot 2 memilih untuk bertahan
                print(f"{self.robot2.name} memilih untuk bertahan.")
            elif action2 == '3':  # Jika aksi 3 (Giveup), robot 2 menyerah
                print(f"{self.robot2.name} menyerah!")
                print(f"{self.robot1.name} menang!")
                return  # Mengakhiri permainan, karena robot 2 menyerah
            
            # Cek apakah robot 1 masih hidup setelah serangan
            if not self.robot1.is_alive():  # Jika robot 1 sudah mati (HP <= 0)
                print(f"{self.robot2.name} menang!")  # Robot 2 menang
                return
            
            # Lanjut ke ronde berikutnya
            self.round += 1  # Menambah ronde permainan

# Contoh penggunaan
robot1 = Robot(name="Atreus", hp=500, attack=10, accuracy=0.85)  # Membuat objek robot pertama
robot2 = Robot(name="Daedalus", hp=750, attack=8, accuracy=0.75)  # Membuat objek robot kedua

game = Game(robot1, robot2)  # Membuat objek game dengan kedua robot
game.start()  # Memulai permainan
