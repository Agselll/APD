import getpass
import os
import time

#var, list, dictionary, dll
m = ["Coffee", "Non Coffee", "Teh", "Snack"]
coffee = ["Americano", "Hazelnut", "Expresso", "Caramel Machiato"]
harga_coffee = [20000, 20000,20000,22000,]
noncoffee = ["Chocolate", "Matcha", "Red Velvet","Taro"]
harga_noncoffee = [22000,22000,22000,22000,] 
teh = ["Lemon Tea", "Lychee Tea"]
harga_teh = [15000,15000,]
snack = ["Chicken Nugget","French Fries","Sosis"]
harga_snack = [15000,15000,15000,]
dictionary = {
'nama_menu' : [],
'harga'     : [],}
jam = time.asctime( time.localtime(time.time()) )
FailsLeft = 3

# Fungsi
def back_to_start():
    input("\nTekan Enter untuk kembali...")
    start()

def back_to_admin():
    input("\nTekan Enter untuk kembali...")
    tampilan_admin()

def back_to_customer():
    input("\nTekan Enter untuk kembali...")
    selamat_datang()

def back_to_pesanan():
    input("\nTekan Enter untuk kembali...")
    proses_pemesanan()
    tampilan_ulang()

def back_to_tampilan_admin2():
    input("\nTekan Enter untuk kembali...")
    tampilan_admin2()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pembelian(a,b):
    global jumlah, total, pajak, total_bayar
    jumlah=int(input("Masukkan jumlah pesanan yang ingin dibeli : "))
    dictionary["nama_menu"] += [a]
    dictionary["harga"] += [b]
    total = sum(dictionary["harga"] * jumlah)
    pajak = total*0.10
    total_bayar = total + pajak
    proses_pemesanan()

def proses_pemesanan():
    clear()
    pesanan("SEDANG DALAM PROSES MEMESAN","-//-","INGIN MELANJUTKAN PESANAN ?","~~~~~~~")

def pesanan(a,b,c,d,uang_bayar = 0,kembalian=0,waktu = 2):
    clear()
    print(f"{'='*80}\n|{a:^78}|\n|{b:^78}|\n{'='*80}")
    print(f"| {'Nama Pelanggan':<22}: {nama_pelanggan:<53}|")
    print(f"| {'Nama Menu':<22}: {str(dictionary['nama_menu']):<53}|")
    print(f"| {'Harga':<22}: Rp.{str(total):<50}|")
    print(f"| {'Pajak':<22}: Rp.{str(pajak):<50}|")
    print(f"| {'Total Bayar':<22}: Rp.{str(total_bayar):<50}|")
    print(f"| {'Uang Bayar':<22}: Rp.{str(uang_bayar):<50}|")
    print(f"| {'Kembalian':<22}: Rp.{str(kembalian):<50}|")
    print(f"| {'Waktu Pembayaran':<22}: {jam:<53}|")
    print(f"{'='*80}\n|{c:^78}|\n|{d:^78}|\n{'='*80}")
    time.sleep(waktu)
    
def pembayaran():
    global uang_bayar,uang_kembali 
    while True :
        try:
            print(f"Total yang perlu dibayar Rp {total_bayar}")
            uang_bayar = int(input("Masukkan jumlah uang bayar : RP. "))
            if uang_bayar < total_bayar:
                print("========================================================================")
                print("| Maaf, uang anda kurang. Silahkan ulangi                              |")
                print("========================================================================")
                continue
            elif uang_bayar == total_bayar or uang_bayar > total_bayar :
                uang_kembali = uang_bayar - total_bayar
                break
        except ValueError:
            error()
            continue

def logout():
    print("========================================================================")
    print("|                        PROGRAM TELAH SELESAI                         |")
    print("========================================================================")
    print("|           TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA            |")
    print("|                     YANG DISUSUN OLEH KELOMPOK 3                     |")
    print("|                      INFORMATIKA A'22 KELAS A'2                      |")
    print("|                                  |||                                 |")
    print("|                         UNIVERSITAS MULAWARMAN                       |")
    print("========================================================================")

def error(a = ""):
    print(f"========================================================================")
    print(f"| Input yang Anda masukkan salah silahkan ulangi {(a):5}               |")
    print(f"========================================================================")

def selamat_datang():
    clear()
    print("========================================================================")
    print("|                            SELAMAT DATANG                            |")
    print("|                                  DI                                  |")
    print("|                          COFFEE SHOP APAYAAAAAAA                     |")
    print("|                                 OLEH                                 |")
    print("|         KELOMPOK 3 - INFORMATIKA 2022 - UNIVERSITAS MULAWARMAN       |")
    print("========================================================================")

def tampilan():
    print("========================================================================")
    print("|                            SELAMAT DATANG                            |")
    print("|                                  DI                                  |")
    print("|                          COFFEE SHOP APAYAAAA                        |")
    print("|                                 OLEH                                 |")
    print("|         KELOMPOK 3 - INFORMATIKA 2022 - UNIVERSITAS MULAWARMAN       |")
    print("========================================================================")
    print("| [1] Login Sebagai Admin                                              |")
    print("| [2] Pesan Menu                                                       |")
    print("| [0] Keluar Program                                                   |")
    print("========================================================================")

def tampilan_admin():
    clear()
    print("========================================================================")
    print("|                        Selamat Datang Admin                          |")
    print("========================================================================")
    print("| [1] Login                                                            |")
    print("| [2] Kembali                                                          |")
    print("========================================================================")

def tampilan_admin2():
    clear()
    print("=========================================================================")
    print("|                        Selamat Datang Admin                           |")
    print("=========================================================================")
    print("| [1] Lihat                                                             |")
    print("| [2] Tambah                                                            |")
    print("| [3] Edit                                                              |")
    print("| [4] Hapus                                                             |")
    print("| [0] Kembali Ke Menu Awal                                              |")
    print("=========================================================================")

def tampilan_ulang():
    print("========================================================================")
    print("| [1] Pesan Menu Lainnya                                               |")
    print("| [2] Ulang Pesanan                                                    |")
    print("| [3] Bayar                                                            |")
    print("========================================================================")
    ulang = (input("Masukkan Pilihan Anda : "))
    if ulang == "3":
        pembayaran()
        pesanan("STRUK INI AKAN MENGHILANG DALAM 15 DETIK","PESANAN ANDA TELAH LUNAS","TERIMAKASIH SUDAH MENGUNJUNGI COFFEE SHOP APAYAAA","SEMOGA BERLANGGANAN!",uang_bayar =str(uang_bayar),kembalian =str(uang_kembali),waktu =15)
        dictionary["nama_menu"].clear()
        dictionary["harga"].clear()
        start()
    elif ulang == "1":
        tampilan_utama()
    elif ulang == "2":
        dictionary["nama_menu"].clear()
        dictionary["harga"].clear()
        tampilan_utama()
    else:
        error()
        back_to_pesanan()
        time.sleep(2)

def tampilan_utama() :
    while True:
        selamat_datang() 
        print(f"\n{'='*60}\n|{'Silahkan Pilih Menu':^58}|\n{'='*60}")
        a=0
        for i in range(len(m)):
            a=a+1
            print(f"| [{a}] {m[i]:<53}|")
        print("============================================================")
        pilih_menuutama = input("Pilih Menu : " )
        if pilih_menuutama == "1":
            tampilan_coffee()
            tampilan_customer_coffee()
            tampilan_ulang()
        elif pilih_menuutama == "2":
            tampilan_noncoffee()
            tampilan_customer_noncoffee()
            tampilan_ulang()
        elif pilih_menuutama == "3":
            tampilan_teh()
            tampilan_customer_teh()  
            tampilan_ulang()  
        elif pilih_menuutama == "4":
            tampilan_snack()
            tampilan_customer_snack()
            tampilan_ulang()
        else:
            clear()
            error()
            back_to_customer()
            selamat_datang()
    
def tampilan_coffee() :
    selamat_datang() 
    print(f"\n{'='*60}\n|{'Silahkan Pilih Menu':^58}|\n{'='*60}")
    a=0
    for i in range(len(coffee)):
        a=a+1
        print(f"| [{a}] {coffee[i]:<35} Rp{harga_coffee[i]:<15}|")
    print("============================================================")
    
def tampilan_noncoffee() :
    selamat_datang() 
    print(f"\n{'='*60}\n|{'Silahkan Pilih Menu':^58}|\n{'='*60}")
    a=0
    for i in range(len(noncoffee)):
        a=a+1
        print(f"| [{a}] {noncoffee[i]:<35} Rp{harga_noncoffee[i]:<15}|")
    print("============================================================")

def tampilan_teh() :
    selamat_datang() 
    print(f"\n{'='*60}\n|{'Silahkan Pilih Menu':^58}|\n{'='*60}")
    a=0
    for i in range(len(teh)):
        a=a+1
        print(f"| [{a}] {teh[i]:<35} Rp{harga_teh[i]:<15}|")
    print("============================================================")

def tampilan_snack() :
    selamat_datang() 
    print(f"\n{'='*60}\n|{'Silahkan Pilih Menu':^58}|\n{'='*60}")
    a=0
    for i in range(len(snack)):
        a=a+1
        print(f"| [{a}] {snack[i]:<35} Rp{harga_snack[i]:<15}|")
    print("============================================================")

def tampilan_customer_coffee():
    try:
        clear()
        tampilan_coffee()
        pilih_coffee = input("Pilih menu : ")
        if int(pilih_coffee) > len(coffee) or int(pilih_coffee) <= 0:
            clear()
            error("pesanan")
            input("\nTekan Enter untuk kembali...")
            tampilan_customer_coffee()
        elif pilih_coffee == str(pilih_coffee):
            pembelian(coffee[int(pilih_coffee) - 1], harga_coffee[int(pilih_coffee) - 1])
    except ValueError:
        clear()
        error("pesanan")
        input("\nTekan Enter untuk kembali...")
        tampilan_customer_coffee()

def tampilan_customer_noncoffee():
    try:
        clear()
        tampilan_noncoffee()
        pilih_noncoffee = input("Pilih menu : ")        
        if int(pilih_noncoffee) > len(noncoffee) or int(pilih_noncoffee) <= 0:
            clear()
            error("pesanan")
            input("\nTekan Enter untuk kembali...")
            tampilan_customer_noncoffee()
        elif pilih_noncoffee == str(pilih_noncoffee):
            pembelian(noncoffee[int(pilih_noncoffee)-1],harga_noncoffee[int(pilih_noncoffee)-1])
    except ValueError:
        clear()
        error("pesanan")
        input("\nTekan Enter untuk kembali...")
        tampilan_customer_noncoffee()   

def tampilan_customer_teh():
    try:
        clear()
        tampilan_teh()
        pilih_teh = input("Pilih menu : ")
        if int(pilih_teh) > len(teh) or int(pilih_teh) <= 0:
            clear()
            error("pesanan")
            input("\nTekan Enter untuk kembali...")
            tampilan_customer_teh()
        elif pilih_teh == str(pilih_teh):
            pembelian(teh[int(pilih_teh)-1],harga_teh[int(pilih_teh)-1])
    except ValueError:
        clear()
        error("pesanan")
        input("\nTekan Enter untuk kembali...")
        tampilan_customer_teh()

def tampilan_customer_snack():
    try:
        clear()
        tampilan_snack()
        pilih_snack = input("Pilih menu : ")
        if int(pilih_snack) > len(snack) or int(pilih_snack) <= 0:
            clear()
            error("pesanan")
            input("\nTekan Enter untuk kembali...")
            tampilan_customer_snack()
        elif pilih_snack == str(pilih_snack):
            pembelian(snack[int(pilih_snack)-1],harga_snack[int(pilih_snack)-1])
    except ValueError:
        clear()
        error("pesanan")
        input("\nTekan Enter untuk kembali...")
        tampilan_customer_snack()

def kembali_admin():
    input("\nTekan Enter untuk kembali : ")
    pilihan_admin()

def pilihan_admin():
    clear() 
    while True:
        tampilan_admin2()
        pilihan_admin = input("Masukkan pilihan anda : ")
        if pilihan_admin == "1":
            clear()
            lihat()
            kembali_admin()
        elif pilihan_admin == "2":
            clear()
            lihat()
            tambah()
            kembali_admin()
        elif pilihan_admin == "3":
            clear()
            lihat()
            edit()
            kembali_admin()
        elif pilihan_admin == "4":
            clear()
            lihat()
            hapus()
            kembali_admin()
        elif pilihan_admin == "0":
            start()
            continue
        else:
            clear()
            error()
            back_to_tampilan_admin2()
            tampilan_admin2()
        
def login_berhasil():
    clear()
    print("\t\t\t  Login Successful..." )
    time.sleep(2)

def login_gagal():
    global FailsLeft
    time.sleep(0.5)
    print("========================================================================")
    print("| USERNAME ATAU PASSWORD YANG ANDA MASUKKAN SALAH SILAHKAN CEK KEMBALI |")
    print("========================================================================")  
    FailsLeft = FailsLeft - 1
    print("Kamu  memiliki " + str(FailsLeft) + " kesempatan ⚠️")
    print("--"*20)
    if FailsLeft == 0:
        clear()
        print("=======================================================================")
        print("|                 UPS!, ANDA SALAH SEBANYAK TIGA KALI                 |")
        print("|               Maaf anda telah terlogout dari program                |")
        print("=======================================================================")
        print()
        quit()
   
#CRUD

def lihat() :
    if len(coffee) == 0:
        print("Tidak Ada Data")
        return
    print("""
===========================================
|               DAFTAR MENU                |
===========================================
|       Nama           |    Price list    |""")
    print("===========================================")
    print("|                  COFFEE                 |")
    print("===========================================")
    a = 0
    b = 0
    c = 0
    d = 0
    for x in range(len(coffee)):
        print(f"[{a+1}] {coffee[x]:<18}\t Rp{harga_coffee[x]:<15}|")
        a=a+1
    print("===========================================")
    print("|               NON-COFFEE                |")
    print("===========================================")
    for y in range(len(noncoffee)):
        print(f"[{b+1}] {noncoffee[y]:<18}\t Rp{harga_noncoffee[y]:<15}|")
        b=b+1
    print("===========================================")
    print("|                   TEH                   |")
    print("===========================================")
    for z in range(len(teh)):
        print(f"[{c+1}] {teh[z]:<18}\t Rp{harga_teh[z]:<15}|")
        c=c+1
    print("===========================================")
    print("|                  SNACK                  |")
    print("===========================================")
    for v in range(len(snack)):
        print(f"[{d+1}] {snack[v]:<18}\t Rp{harga_snack[v]:<15}|")
        d=d+1
    print("===========================================")

def tambah() :
    print("Coffee=1 \t Non-Coffe=2 \t Teh=3 \t Snack=4 ")
    pilih_tambah = input("Masukkan Indeks Menu Yang Ingin Ditambah : ")
    tambah = input("Masukkan Menu Baru : ")
    tambah_harga = int(input("Masukkan Harga Baru : "))
    if pilih_tambah == "1":
        coffee.append(tambah)
        harga_coffee.append(tambah_harga)
        print("Menu Berhasil Ditambah")
        return
    elif pilih_tambah == "2":
        noncoffee.append(tambah)
        harga_noncoffee.append(tambah_harga)
        print("Menu Berhasil Ditambah")
        return
    elif pilih_tambah == "3":
        teh.append(tambah)
        harga_teh.append(tambah_harga)
        print("Menu Berhasil Ditambah")
        return
    elif pilih_tambah == "4":
        snack.append(tambah)
        harga_snack.append(tambah_harga)
        print("Menu Berhasil Ditambah")
        return

def edit() :
    print("Coffee=1 \t Non-Coffe=2 \t Teh=3 \t Snack=4 ")
    pilih_update = input("Masukkan Indeks Menu Yang Ingin update : ")
    if pilih_update == "1":
        print("Masukkan ID(Indeks) Menu yang ingin update")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        coffee[indeks] = input ("Masukkan menu baru : ")
        harga_coffee[indeks] = int(input("Masukkan harga baru : "))
        print("Menu Berhasil diupdate")
        return
    elif pilih_update == "2":
        print("Masukkan ID(Indeks) Menu yang ingin update")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        noncoffee[indeks] = input ("Masukkan menu baru : ")
        harga_noncoffee[indeks] = int(input("Masukkan harga baru : "))
        print("Menu Berhasil diupdate")
        return
    elif pilih_update == "3":
        print("Masukkan ID(Indeks) Menu yang ingin update")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        teh[indeks] = input ("Masukkan menu baru : ")
        harga_teh[indeks] = int(input("Masukkan harga baru : "))
        print("Menu Berhasil diupdate")
        return
    elif pilih_update == "4":
        print("Masukkan ID(Indeks) Menu yang ingin update")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        snack[indeks] = input ("Masukkan menu baru : ")
        harga_snack[indeks] = int(input("Masukkan harga baru : "))
        print("Menu Berhasil diupdate")
        return

def hapus() :
    print("Coffee=1 \t Non-Coffe=2 \t Teh=3 \t Snack=4 ")
    pilih_hapus = input("Masukkan Indeks Menu Yang Ingin Dihapus : ")
    if pilih_hapus == "1":
        print("Masukkan ID(Indeks) Menu yang ingin dihapus")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        coffee.remove(coffee[indeks])
        harga_coffee.remove(harga_coffee[indeks])
        print("Menu Berhasil dihapus")
        return
    elif pilih_hapus == "2":
        print("Masukkan ID(Indeks) Menu yang ingin dihapus")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        noncoffee.remove(noncoffee[indeks])
        harga_noncoffee.remove(harga_noncoffee[indeks])
        print("Menu Berhasil dihapus")
        return
    elif pilih_hapus == "3":
        print("Masukkan ID(Indeks) Menu yang ingin dihapus")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        teh.remove(teh[indeks])
        harga_teh.remove(harga_teh[indeks])
        print("Menu Berhasil dihapus")
        return
    elif pilih_hapus == "4":
        print("Masukkan ID(Indeks) Menu yang ingin dihapus")
        ind = int(input("Inputkan ID Menu : "))
        indeks = ind - 1
        snack.remove(snack[indeks])
        harga_snack.remove(harga_snack[indeks])
        print("Menu Berhasil dihapus")
        return

def start():
    clear()
    tampilan()
    pilihan_menu=str(input("Masukkan Pilihan Anda : "))
    Username = "a"
    Password = "1"
    if pilihan_menu == "1":
        tampilan_admin()
        login_admin = input("Pilih : ")
        if login_admin == "1":
            clear()
            print("Silahkan masukkan username dan password anda")
            LoginAdmin  = input("Username : ")
            PwAdmin     = getpass.getpass("Password : ")
            if LoginAdmin == Username and PwAdmin == Password:
                login_berhasil()   
                pilihan_admin()            
            else:
                login_gagal()
                time.sleep(4)
                start()     
        elif login_admin == "2":
            clear()
            start()
        else:
            clear()
            error() 
            back_to_admin()
            start()
    elif pilihan_menu == "2":
        global nama_pelanggan
        clear()
        selamat_datang()
        nama_pelanggan = input("Masukkan Nama Pelanggan : ")
        clear()
        tampilan_utama() 
    elif pilihan_menu == "0":
        clear()
        time.sleep(1)
        logout()
        exit()
    else:
        clear()
        error()
        back_to_start()

start()