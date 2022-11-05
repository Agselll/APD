import os
import getpass
import time
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pesanan():
    print(f"\n{'='*80}\n|{'PEMBAYARAN TELAH SELESAI':^78}|\n{'='*80}")
    print(f"| {'Nama Pelanggan':<22}: {nama_pelanggan:<53}|")
    print(f"| {'Total Pesanan':<22}: {total:<53}|")
    print(f"{'='*80}\n|{'TERIMA KASIH ATAS KUNJUNGANNYA':^78}|\n|{'SEMOGA BERLANGGANAN':^78}|\n{'='*80}")
    

menu=[
    ["nasi ayam geprek", 15000 ],
    ["nasi pecel", 15000 ],
    ["nasi campur", 12000 ],
    ["nasi kuning", 12000 ],
    ["es teh", 4000 ],
    ["es jeruk", 4000 ],
    ["es extrajoss susu", 5000 ],
    ["air mineral", 4000 ],
]

def option_menu1():
    print(f"\n{'='*50}\n|{'Silakan Pilih Menu':^48}|\n{'='*50}")
    for index, m in enumerate(menu):
        print(f"|{index+1:^6}| {m[0]:<25}Rp {m[1]:<12}|")
    print("="*50)
    
              

def admin():
    print("========================================================================")
    print("|                    SELAMAT DATANG AGSEL YANG GANTENG                 |")
    print("|         -----------------------------------------------------        |")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("========================================================================")   
    nama = "agsel"
    kunci = "apaya"
    salah = 0
    while True :
        username = getpass.getpass("masukkan username : ")
        password = getpass.getpass("masukkan password : ")

        if username == nama and password == kunci :
           clear()
           print("|         -----------------------------------------------------        |")
           print("|                          Anda berhasil login                         |")
           print("|         -----------------------------------------------------        |")
           print("|                      Apa yang ingin Agsel lakukan?                   |")
           print("|         -----------------------------------------------------        |")
           break

        else :
            salah += 1
            print("|         -----------------------------------------------------        |")
            print("|                      username atau password salah                    |")
            print("|         -----------------------------------------------------        |")
            if salah == 3 : 
                print("========================================================================")
                print("|                    SORRY SEPERTINYA ANDA BUKAN AGSEL                 |")
                print("========================================================================")  
                exit()


def admin_menu():
    while True:
        print("")
        print("\t============================================================") 
        print("\t| [1].Lihat menu                                           |")
        print("\t| [2].Tambah menu                                          |")
        print("\t| [3].Ubah harga menu                                      |")
        print("\t| [4].Hapus menu                                           |")
        print("\t| [0].Keluar Program                                       |")
        print("\t============================================================")
        menu=int(input("Masukkan Pilihan : "))
        if menu == 1:
            time.sleep(0.5)
            lihat()
            time.sleep(2)
        elif menu == 2:
            tambah()
        elif menu == 3:
            ubah_harga()
        elif menu == 4:
            hapus()
        elif menu == 0:
            clear()
            exit()
        else:
            clear()
            error()
            continue
                
def lihat():
    clear()
    option_menu1()

def tambah():
    nama_menu = [
                    input("Masukkan menu baru : "), 
                    int(input("Masukkan harga : "))
                ]
    menu.append(nama_menu)
    clear()
    print(nama_menu,"telah di tambahkan")

def ubah_harga():
    lihat()
    ubah_harga = input("Masukkan menu yang ingin diubah harganya : ")
    for indeks, data in enumerate (menu):
        if data[0] == ubah_harga:
            ubah_harga = data
            indeks_menu = indeks
        else :
            continue
        ubah_harga = int(input(f"Harga diubah menjadi : "))
        menu[indeks_menu][1] = ubah_harga
    clear()

def hapus():
    lihat()
    hapus_menu = input("Masukkan nama menu yang ingin dihapus : ")
    for indeks, data in enumerate (menu):
        if data[0] == hapus_menu:
            nama_menu = data
            hapus_menu = indeks
        else:
            continue
    print(f"menu {nama_menu} berhasil dihapus")
    menu.remove(nama_menu)
    clear()



def karyawan():
    print("========================================================================")
    print("|            SELAMAT DATANG KARYAWAN YANG GANTENG DAN CANTIK           |")
    print("|         -----------------------------------------------------        |")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("========================================================================") 
    nama = "lalala"
    kunci = "apaya"
    salah = 0
    while True :
        username = getpass.getpass("masukkan username : ")
        password = getpass.getpass("masukkan password : ")

        if username == nama and password == kunci :
           clear()
           print("|         -----------------------------------------------------        |")
           print("|                          Anda berhasil login                         |")
           print("|         -----------------------------------------------------        |")
           print("|                   Silahkan tambahkan pesanan customer                |")
           print("|         -----------------------------------------------------        |")
           break

        else :
            salah += 1
            print("|         -----------------------------------------------------        |")
            print("|                      username atau password salah                    |")
            print("|         -----------------------------------------------------        |")
            if salah == 3 : 
                print("========================================================================")
                print("|                  SORRY SEPERTINYA ANDA BUKAN KARYAWAN                |")
                print("========================================================================")  
                exit()
    

def error():
    print("========================================================================")
    print("|               Pilihan anda tidak valid silahkan ulangi               |")
    print("========================================================================")


while True:
    clear()
    print("========================================================================")
    print("|                             SELAMAT DATANG                           |")
    print("|                                   DI                                 |")
    print("|                           WARUNG MAKAN APAYA                         |")
    print("========================================================================")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Login Sebagai Admin                                              |")
    print("| [2] Login Sebagai Karyawan                                           |")
    print("========================================================================")  
    pilihan_menu=int(input("Masukkan Pilihan Anda : "))
    if pilihan_menu == 1:   
        clear()
        admin()
        time.sleep(0.5)
        admin_menu()
        break
    elif pilihan_menu == 2:
        clear()
        time.sleep(0.5)
        karyawan()
        option_menu1()
        print("KETIK SELESAI UNTUK MENGAKHIRI PESANAN CUSTOMER\n")
        nama_pelanggan = input("Nama pelanggan : ") 
        total = 0
        while True:
            pilihan = input("Silahkan pilih menu : ")
            if pilihan == "SELESAI" or pilihan == "selesai":
                pesanan()
                break
            else:
                jumlah  = int(input("Jumlah Pesanan : "))
                for index, m in enumerate(menu):
                    if int(pilihan) == index+1:
                        harga = m[1]*jumlah
                    else:
                        continue
            print (f"Total          : {harga}")
            total += harga
        break
    else:
        error()
        
