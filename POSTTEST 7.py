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
    time.sleep(8)

menu = {
    1 : {"menu" : "nasi pecel", "harga" : 15000},
    2 : {"menu" : "nasi campur", "harga" : 12000},
    3 : {"menu" : "nasi kuning", "harga" : 12000},
    4 : {"menu" : "es teh", "harga" : 4000},
    5 : {"menu" : "es jeruk", "harga" : 4000},
    6 : {"menu" : "air mineral", "harga" : 4000}, 
}


def option_menu1():
    print('========================================================')
    print('|                   SILAHKAN PILIH MENU                |')
    print('========================================================')
    a=0
    for key in menu:
            a+=1
            print(f"|{a:^6}| {menu[key]['menu']:<16}Rp {menu[key]['harga']:<27}|")
    print('========================================================')

def admin():
    print("========================================================================")
    print("|                    SELAMAT DATANG AGSEL YANG GANTENG                 |")
    print("|         -----------------------------------------------------        |")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("========================================================================")   
    nama = "a"
    kunci = "1"
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
        print("\t| [0].Kembali Ke Menu Awal                                 |")
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
            break
        else:
            clear()
            error()
            continue
def isExist(value):
    for abc in menu:
        if menu[abc]["menu"] == value:
            return True, abc
        else:
            continue
    return False, "Data tidak ada"

def lihat():
    clear()
    option_menu1()

def tambah():
    tambah_menu = {
                    "menu":input("Masukkan menu : "),
                    "harga":int(input("Masukkan harga : "))
                }
    tambah_menu['menu'] = tambah_menu['menu']
    key = len(menu) + 1
    menu.update({key : tambah_menu})
    clear()
    print(tambah_menu,"telah di tambahkan")

def ubah_harga():
    lihat()
    ubah_menu = input("Masukkan menu yang ingin diubah harganya : ")
    ubah_menu = ubah_menu
    bol, key = isExist(ubah_menu)
    if bol:
        ubah_harga = int(input(f"Harga diubah menjadi : "))
        clear()
        print(ubah_menu,"harganya telah di ubah")
        menu[key]["harga"] = ubah_harga
    else :
        print(key)

def hapus():
    lihat()
    hapus_menu = input("Masukkan menu yang ingin dihapus : ")
    hapus_menu = hapus_menu
    clear()
    print(hapus_menu,"telah dihapus")
    bol, key = isExist(hapus_menu)
    if bol:
        del menu[key]
        

def karyawan():
    print("========================================================================")
    print("|            SELAMAT DATANG KARYAWAN YANG GANTENG DAN CANTIK           |")
    print("|         -----------------------------------------------------        |")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("========================================================================") 
    nama = "a"
    kunci = "2"
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
    elif pilihan_menu == 2:
        clear()
        time.sleep(0.5)
        karyawan()
        while True:
            clear()
            option_menu1()
            print("KETIK SELESAI UNTUK MENGAKHIRI PESANAN CUSTOMER")
            print("(ketik nama menu bukan indeks menu)\n")
            nama_pelanggan = input("Nama pelanggan : ") 
            total = 0
            while True:
                pilihan = input("Silahkan pilih menu : ")
                if pilihan == "SELESAI" or pilihan == "selesai":
                    pesanan()
                    break
                    
                else:
                    jumlah  = int(input("Jumlah Pesanan : "))
                    for nama in menu:
                        if menu[nama]['menu'] == pilihan:
                            harga = menu[nama]['harga']*jumlah
                        else:
                            continue
                        print (f"Total          : {harga}")
                        print("="*30)
                        total += harga
    else:
        error()
        
