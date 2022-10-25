import os
import time

def clear():
    os.system("cls," if os.name == "nt" else "clear")

# SUHU
def suhu():   
    print("========================================================================")
    print("|                             KONVERSI SUHU                            |")
    print("========================================================================")
    # MASUKKAN INPUTAN CELCIUS AWAL
    celcius = float(input('Masukan suhu dalam celcius : '))
    print("suhu adalah\t \t \t ",celcius, "°Celcius")
    # KONVERSI REAMUR
    reamur = (4/5) * celcius
    print("suhu dalam reamur adalah\t ",reamur, "°Reamur")
    # KONVERSI CELCIUS KE FAHRENHEIT
    fahrenheit = ((9/5) * celcius) + 32
    print("suhu dalam fahrenheit adalah\t ",fahrenheit, "°Fahrenheit")
    # KONVERSI CELCIUS KE KELVIN
    kelvin = celcius + 273
    print("suhu dalam kelvin adalah\t ",kelvin, "°Kelvin")

# BIODATA
def biodata():
     while True:
        dictionary = {
            "nama" : "",
            "nim" : "",
            "hobi" : "",
            "angkatan" : "",
            "ukuran sepatu" : ""
            }
        # TAMPILAN SAAT MENGISI BIODATA
        print("========================================================================")
        print("|                     SILAHKAN ISI BIODATA MAHASISWA                   |")
        print("========================================================================")
        try:
             nama = str(input("Masukkan Nama\t \t: "))
        except ValueError:
                print("=============== UPSSS, NILAI YANG ANDA MASUKKAN SALAH!!!================")
                biodata()
        try:
             nim = int(input("Masukkan NIM\t \t: "))
        except ValueError:
                print("========== UPSSS, NILAI YANG ANDA MASUKKAN SALAH!!!==========")
                biodata()
        try:
             hobi = str(input("Masukkan Hobi\t \t: "))
        except ValueError:
                print("========== UPSSS, NILAI YANG ANDA MASUKKAN SALAH!!!==========")
                biodata()
        try:
             angkatan = int(input("Masukkan Angkatan\t: "))
        except ValueError:
                print("========== UPSSS, NILAI YANG ANDA MASUKKAN SALAH!!!==========")
                biodata()
        try:
             ukuran_sepatu = float(input("Masukkan Ukuran Sepatu\t: "))
        except ValueError:
                print("========== UPSSS, NILAI YANG ANDA MASUKKAN SALAH!!!==========")
                biodata()
        dictionary["Nama"] = nama
        dictionary["Nim"] = nim
        dictionary["Hobi"] = hobi
        dictionary["Angkatan"] = angkatan
        dictionary["Ukuran Sepatu"] = ukuran_sepatu
        clear()
        time.sleep(0.5)

        # TAMPILAN SAAT BIODATA TELAH DI INPUT
        print("=========================================================================")
        print("|                             BIODATA ANDA                              |")
        print("=========================================================================")
        print(f"""                                  
Nama\t     : {dictionary["Nama"]}
Nim\t     : {dictionary["Nim"]}
Hobi\t     : {dictionary["Hobi"]}
Angkatan     : {dictionary["Angkatan"]} 
Ukuran Sepatu: {dictionary["Ukuran Sepatu"]}
""")
        break


# KETIKA TERJADI ERROR PADA TAMPILAN AWAL
def error():
    print("========================================================================")
    print("|        UPS, SALAHHHH!! ANGKA YANG ANDA MASUKKAN TIDAK VALID!         |")
    print("========================================================================")
   
# KETIKA LOGOUT DARI PROGRAM
def logout():
    print("========================================================================")
    print("|                        PROGRAM TELAH SELESAI                         |")
    print("========================================================================")
    print("|           TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA            |")
    print("|                            YANG DISUSUN OLEH                         |")
    print("|                       AGSEL FALANA SUPARLAN PUTRA                    |")
    print("|                             INFORMATIKA A'22                         |")
    print("|                                2209106046                            |")
    print("========================================================================")

#PERULANGAN TAMPILAN MENU
while True:
    print("========================================================================")
    print("|                             SELAMAT DATANG                           |")
    print("|                                   DI                                 |")
    print("|                      PROGRAM SEDERHANA POSTTEST 3                    |")
    print("|                                  OLEH                                |")
    print("|                      AGSEL FALANA SUPARLAN PUTRA                     |")
    print("========================================================================")
    print("| [1] Konversi Suhu                                                    |")
    print("| [2] Biodata Mahasiswa                                                |")
    print("| [3] Keluar Program                                                   |")
    print("========================================================================")

    # INPUTAN UNTUK TAMPILAN MENU
   
    pilihan_menu= int(input("Masukkan Pilihan : "))
    if (pilihan_menu == 1):
        clear()
        time.sleep(0.5)
        suhu()
        time.sleep(0.5)
    if (pilihan_menu == 2):
        clear()
        time.sleep(0.5)
        biodata()
        time.sleep(0.5)
    if (pilihan_menu == 3):
        clear()
        time.sleep(0.5)
        logout()
        time.sleep(0.5)
        break
    if(pilihan_menu >= 4):
        clear()
        time.sleep(0.5)
        error()
        time.sleep(0.5)