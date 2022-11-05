###################################### LIBRARY ######################################
import os
import time
################################## FUNCTION CLEAR ###################################
def clear():
    os.system("cls" if os.name == "nt" else "clear")

############################### KONVERSI KILOMETER ##################################
def back_to_KM():
    print("\n")
    input("Tekan Enter untuk kembali...")
    clear()
    konversi_KM()

def konversi_KM():
    print("========================================================================")
    print("|                          KONVERSI KILOMETER                          |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi KILOMETER ke HEKTOMETER                                 |")
    print("| [2] Konversi KILOMETER ke METER                                      |")
    print("| [3] Konversi KILOMETER ke DESIMETER                                  |")
    print("| [4] Konversi KILOMETER ke CENTIMETER                                 |")
    print("| [5] Konversi KILOMETER ke MILIMETER                                  |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

def KM_ke_HM():
    print("========================================================================")
    print("|                  KONVERSI KILOMETER KE HEKTOMETER                    |")
    print("========================================================================")
    KM= float(input("Masukkan angka yang ingin di konversikan (Km) : "))
    print("Angka dalam kilometer adalah : ", KM, "Km")
    KM_ke_Hektometer= KM * 10
    print("Jadi, Jika", KM, "Km dikonversikan menjadi", KM_ke_Hektometer, "Hektometer" )
    print("\t=================================================================")
    back_to_KM()

def KM_ke_M():
    print("========================================================================")
    print("|                    KONVERSI KILOMETER KE METER                       |")
    print("========================================================================")
    KM= float(input("Masukkan angka yang ingin di konversikan (Km) : "))
    print("Angka dalam kilometer adalah : ", KM, "Km")
    KM_ke_Meter= KM * 1000
    print("Jadi, Jika", KM, "Km dikonversikan menjadi", KM_ke_Meter, "Meter" )
    print("\t=================================================================")
    back_to_KM()

def KM_ke_DM():
    print("========================================================================")
    print("|                  KONVERSI KILOMETER KE DESIMETER                     |")
    print("========================================================================")
    KM= float(input("Masukkan angka yang ingin di konversikan (Km) : "))
    print("Angka dalam kilometer adalah : ", KM, "Km")
    KM_ke_Meter= KM * 10000
    print("Jadi, Jika", KM, "Km dikonversikan menjadi", KM_ke_Meter, "Desimeter" )
    print("\t=================================================================")
    back_to_KM()

def KM_ke_CM():
    print("========================================================================")
    print("|                 KONVERSI KILOMETER KE CENTIMETER                     |")
    print("========================================================================")
    KM= float(input("Masukkan angka yang ingin di konversikan (Km) : "))
    print("Angka dalam kilometer adalah : ", KM, "Km")
    KM_ke_CM= KM * 100000
    print("Jadi, Jika", KM, "Km dikonversikan menjadi", KM_ke_CM, "Centimeter" )
    print("\t=================================================================")
    back_to_KM()

def KM_ke_MM():
    print("========================================================================")
    print("|                  KONVERSI KILOMETER KE MILIMETER                     |")
    print("========================================================================")
    KM= float(input("Masukkan angka yang ingin di konversikan (Km) : "))
    print("Angka dalam kilometer adalah : ", KM, "Km")
    KM_ke_MM= KM * 1000000
    print("Jadi, Jika", KM, "Km dikonversikan menjadi", KM_ke_MM, "Milimeter" )
    print("\t=================================================================")
    back_to_KM()

################################# KONVERSI HM ######################################
def back_to_HM():
    print("\n")
    input("Tekan Enter untuk kembali...")
    clear()
    konversi_HM()

def konversi_HM():
    print("========================================================================")
    print("|                          KONVERSI HEKTOMETER                         |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi HEKTOMETER ke KILOMETER                                 |")
    print("| [2] Konversi HEKTOMETER ke METER                                     |")
    print("| [3] Konversi HEKTOMETER ke DESIMETER                                 |")
    print("| [4] Konversi HEKTOMETER ke CENTIMETER                                |")
    print("| [5] Konversi HEKTOMETER ke MILIMETER                                 |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

def HM_ke_KM():
    print("========================================================================")
    print("|                  KONVERSI HEKTOMETER KE KILOMETER                    |")
    print("========================================================================")
    HM= float(input("Masukkan angka yang ingin di konversikan (HM) : "))
    print("Angka dalam hektometer adalah : ", HM, "HM")
    HM_ke_KM= HM / 10
    print("Jadi, Jika", HM, "HM dikonversikan menjadi", HM_ke_KM, "Kilometer" )
    print("\t=================================================================")
    back_to_HM()

def HM_ke_M():
    print("========================================================================")
    print("|                    KONVERSI HEKTOMETER KE METER                      |")
    print("========================================================================")
    HM= float(input("Masukkan angka yang ingin di konversikan (HM) : "))
    print("Angka dalam hektometer adalah : ", HM, "HM")
    HM_ke_M= HM * 100
    print("Jadi, Jika", HM, "HM dikonversikan menjadi", HM_ke_M, "Meter" )
    print("\t=================================================================")
    back_to_HM()

def HM_ke_DM():
    print("========================================================================")
    print("|                  KONVERSI HEKTOMETER KE DESIMETER                    |")
    print("========================================================================")
    HM= float(input("Masukkan angka yang ingin di konversikan (HM) : "))
    print("Angka dalam hektometer adalah : ", HM, "HM")
    HM_ke_DM = HM * 1000
    print("Jadi, Jika", HM, "HM dikonversikan menjadi", HM_ke_DM , "Desimeter" )
    print("\t=================================================================")
    back_to_DM()

def HM_ke_CM():
    print("========================================================================")
    print("|                  KONVERSI HEKTOMETER KE CENTIMETER                   |")
    print("========================================================================")
    HM= float(input("Masukkan angka yang ingin di konversikan (HM) : "))
    print("Angka dalam hektometer adalah : ", HM, "HM")
    HM_ke_CM= HM * 10000
    print("Jadi, Jika", HM, "HM dikonversikan menjadi", HM_ke_CM, "Centimeter" )
    print("\t=================================================================")
    back_to_HM()

def HM_ke_MM():
    print("========================================================================")
    print("|                  KONVERSI HEKTOMETER KE MILIMETER                    |")
    print("========================================================================")
    HM= float(input("Masukkan angka yang ingin di konversikan (HM) : "))
    print("Angka dalam hektometer adalah : ", HM, "HM")
    HM_ke_MM= HM * 100000
    print("Jadi, Jika", HM, "HM dikonversikan menjadi", HM_ke_MM, "Milimeter" )
    print("\t=================================================================")
    back_to_HM()

#################################### KONVERSI M #####################################
def back_to_M():
    print("\n")
    input("Tekan Enter untuk kembali... ")
    clear()
    konversi_M()

def konversi_M():
    print("========================================================================")
    print("|                            KONVERSI METER                            |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi METER ke KILOMETER                                      |")
    print("| [2] Konversi METER ke HEKTOMETER                                     |")
    print("| [3] Konversi METER ke DESIMETER                                      |")
    print("| [4] Konversi METER ke CENTIMETER                                     |")
    print("| [5] Konversi METER ke MILIMETER                                      |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

def M_ke_KM():
    print("========================================================================")
    print("|                     KONVERSI METER KE KILOMETER                      |")
    print("========================================================================")
    M= float(input("Masukkan angka yang ingin di konversikan (m) : "))
    print("Angka dalam meter adalah : ", M, "m")
    M_ke_KM= M / 1000
    print("Jadi, Jika", M, "m dikonversikan menjadi", M_ke_KM, "Kilometer" )
    print("\t=================================================================")
    back_to_M()


def M_ke_HM():
    print("========================================================================")
    print("|                     KONVERSI METER KE HEKTOMETER                     |")
    print("========================================================================")
    M= float(input("Masukkan angka yang ingin di konversikan (m) : "))
    print("Angka dalam meter adalah : ", M, "m")
    M_ke_HM= M / 100
    print("Jadi, Jika", M, "m dikonversikan menjadi", M_ke_HM, "Hektometer" )
    print("\t=================================================================")
    back_to_M()

def M_ke_DM():
    print("========================================================================")
    print("|                     KONVERSI METER KE DESIMETER                      |")
    print("========================================================================")
    M= float(input("Masukkan angka yang ingin di konversikan (m) : "))
    print("Angka dalam meter adalah : ", M, "m")
    M_ke_DM= M * 10
    print("Jadi, Jika", M, "m dikonversikan menjadi", M_ke_DM, "Desimeter" )
    print("\t=================================================================")
    back_to_M()

def M_KE_CM():
    print("========================================================================")
    print("|                    KONVERSI METER KE CENTIMETER                      |")
    print("========================================================================")
    M= float(input("Masukkan angka yang ingin di konversikan (m) : "))
    print("Angka dalam meter adalah : ", M, "m")
    M_KE_CM= M * 100
    print("Jadi, Jika", M, "m dikonversikan menjadi", M_KE_CM, "Centimeter" )
    print("\t=================================================================")
    back_to_M()

def M_KE_MM():
    print("========================================================================")
    print("|                     KONVERSI METER KE MILIMETER                      |")
    print("========================================================================")
    M= float(input("Masukkan angka yang ingin di konversikan (m) : "))
    print("Angka dalam meter adalah : ", M, "m")
    M_KE_MM= M * 1000
    print("Jadi, Jika", M, "m dikonversikan menjadi", M_KE_MM, "Milimeter" )
    print("\t=================================================================")
    back_to_M()

############################### KONVERSI DESIMETER ##################################
def back_to_DM():
    print("\n")
    input("Tekan Enter untuk kembali...")
    clear()
    konversi_DM()

def konversi_DM():
    print("========================================================================")
    print("|                          KONVERSI DESIMETER                          |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi DESIMETER ke KILOMETER                                  |")
    print("| [2] Konversi DESIMETER ke HEKTOMETER                                 |")
    print("| [3] Konversi DESIMETER ke METER                                      |")
    print("| [4] Konversi DESIMETER ke CENTIMETER                                 |")
    print("| [5] Konversi DESIMETER ke MILIMETER                                  |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

def DM_ke_KM():
    print("========================================================================")
    print("|                   KONVERSI DESIMETER KE KILOMETER                    |")
    print("========================================================================")
    DM= float(input("Masukkan angka yang ingin di konversikan (DM) : "))
    print("Angka dalam desimeter adalah : ", DM, "DM")
    DM_ke_KM= DM / 10000
    print("Jadi, Jika", DM, "DM dikonversikan menjadi", DM_ke_KM, "Kilometer" )
    print("\t=================================================================")
    back_to_DM()

def DM_ke_HM():
    print("========================================================================")
    print("|                   KONVERSI DESIMETER KE HEKTOMETER                   |")
    print("========================================================================")
    DM= float(input("Masukkan angka yang ingin di konversikan (DM) : "))
    print("Angka dalam desimeter adalah : ", DM, "DM")
    DM_ke_HM= DM / 1000
    print("Jadi, Jika", DM, "DM dikonversikan menjadi", DM_ke_HM, "Hektometer" )
    print("\t=================================================================")
    back_to_DM()

def DM_ke_M():
    print("========================================================================")
    print("|                     KONVERSI DESIMETER KE METER                      |")
    print("========================================================================")
    DM= float(input("Masukkan angka yang ingin di konversikan (DM) : "))
    print("Angka dalam desimeter adalah : ", DM, "DM")
    DM_ke_M= DM / 10
    print("Jadi, Jika", DM, "DM dikonversikan menjadi", DM_ke_M, "Meter" )
    print("\t=================================================================")
    back_to_DM()

def DM_ke_CM():
    print("========================================================================")
    print("|                   KONVERSI DESIMETER KE CENTIMETER                   |")
    print("========================================================================")
    DM= float(input("Masukkan angka yang ingin di konversikan (DM) : "))
    print("Angka dalam desimeter adalah : ", DM, "DM")
    DM_ke_CM= DM * 10
    print("Jadi, Jika", DM, "DM dikonversikan menjadi", DM_ke_CM, "Centimeter" )
    print("\t=================================================================")
    back_to_DM()

def DM_ke_MM():
    print("========================================================================")
    print("|                   KONVERSI DESIMETER KE MILIMETER                    |")
    print("========================================================================")
    DM= float(input("Masukkan angka yang ingin di konversikan (DM) : "))
    print("Angka dalam desimeter adalah : ", DM, "DM")
    DM_ke_MM= DM * 100
    print("Jadi, Jika", DM, "DM dikonversikan menjadi", DM_ke_MM, "Milimeter" )
    print("\t=================================================================")
    back_to_DM()

################################# KONVERSI CENTIMETER ###############################
def back_to_CM():
    print("\n")
    input("Tekan Enter untuk kembali... ")
    clear()
    konversi_CM()

def konversi_CM():
    print("========================================================================")
    print("|                         KONVERSI CENTIMETER                          |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi CENTIMETER ke KILOMETER                                 |")
    print("| [2] Konversi CENTIMETER ke HEKTOMETER                                |")
    print("| [3] Konversi CENTIMETER ke METER                                     |")
    print("| [4] Konversi CENTIMETER ke DESIMETER                                 |")
    print("| [5] Konversi CENTIMETER ke MILIMETER                                 |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

def CM_ke_KM():
    print("========================================================================")
    print("|                   KONVERSI CENTIMETER KE KILOMETER                   |")
    print("========================================================================")
    CM= float(input("Masukkan angka yang ingin di konversikan (Cm) : "))
    print("Angka dalam centimeter adalah : ", CM, "Cm")
    CM_ke_KM= CM / 100000
    print("Jadi, Jika", CM, "Cm dikonversikan menjadi", CM_ke_KM, "Kilometer" )
    print("\t=================================================================")
    back_to_CM()

def CM_ke_HM():
    print("========================================================================")
    print("|                   KONVERSI CENTIMETER KE HEKTOMETER                  |")
    print("========================================================================")
    CM= float(input("Masukkan angka yang ingin di konversikan (Cm) : "))
    print("Angka dalam centimeter adalah : ", CM, "Cm")
    CM_ke_HM= CM / 10000
    print("Jadi, Jika", CM, "Cm dikonversikan menjadi", CM_ke_HM, "Hektometer" )
    print("\t=================================================================")
    back_to_CM()

def CM_ke_M():
    print("========================================================================")
    print("|                     KONVERSI CENTIMETER KE METER                     |")
    print("========================================================================")
    CM= float(input("Masukkan angka yang ingin di konversikan (Cm) : "))
    print("Angka dalam centimeter adalah : ", CM, "Cm")
    CM_ke_M= CM / 100
    print("Jadi, Jika", CM, "Cm dikonversikan menjadi", CM_ke_M, "Meter" )
    print("\t=================================================================")
    back_to_CM()

def CM_ke_DM():
    print("========================================================================")
    print("|                   KONVERSI CENTIMETER KE DESIMETER                   |")
    print("========================================================================")
    CM= float(input("Masukkan angka yang ingin di konversikan (Cm) : "))
    print("Angka dalam centimeter adalah : ", CM, "Cm")
    CM_ke_DM= CM / 10
    print("Jadi, Jika", CM, "Cm dikonversikan menjadi", CM_ke_DM, "Desimeter" )
    print("\t=================================================================")
    back_to_CM()

def CM_ke_MM():
    print("========================================================================")
    print("|                   KONVERSI CENTIMETER KE MILIMETER                   |")
    print("========================================================================")
    CM= float(input("Masukkan angka yang ingin di konversikan (Cm) : "))
    print("Angka dalam centimeter adalah : ", CM, "Cm")
    CM_ke_MM= CM * 10
    print("Jadi, Jika", CM, "Cm dikonversikan menjadi", CM_ke_MM, "Milimeter" )
    print("\t=================================================================")
    back_to_CM()

############################### KONVERSI MILIMETER ##################################
def back_to_MM():
    print("\n")
    input("Tekan Enter untuk kembali...")
    clear()
    konversi_MM()

def konversi_MM():
    print("========================================================================")
    print("|                          KONVERSI MILIMETER                          |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi MILIMETER ke KILOMETER                                  |")
    print("| [2] Konversi MILIMETER ke HEKTOMETER                                 |")
    print("| [3] Konversi MILIMETER ke METER                                      |")
    print("| [4] Konversi MILIMETER ke DESIMETER                                  |")
    print("| [5] Konversi MILIMETER ke CENTIMETER                                 |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

def MM_ke_KM():
    print("========================================================================")
    print("|                   KONVERSI MILIMETER KE KILOMETER                    |")
    print("========================================================================")
    MM= float(input("Masukkan angka yang ingin di konversikan (mm) : "))
    print("Angka dalam milimeter adalah : ", MM, "mm")
    MM_ke_KM= MM / 1000000
    print("Jadi, Jika", MM, "mm dikonversikan menjadi", MM_ke_KM, "Kilometer" )
    print("\t=================================================================")
    back_to_MM()

def MM_ke_HM():
    print("========================================================================")
    print("|                   KONVERSI MILIMETER KE HEKTOMETER                   |")
    print("========================================================================")
    MM= float(input("Masukkan angka yang ingin di konversikan (mm) : "))
    print("Angka dalam milimeter adalah : ", MM, "mm")
    MM_ke_HM= MM / 100000
    print("Jadi, Jika", MM, "mm dikonversikan menjadi", MM_ke_HM, "Hektometer" )
    print("\t=================================================================")
    back_to_MM()

def MM_ke_M():
    print("========================================================================")
    print("|                     KONVERSI MILIMETER KE METER                      |")
    print("========================================================================")
    MM= float(input("Masukkan angka yang ingin di konversikan (mm) : "))
    print("Angka dalam milimeter adalah : ", MM, "mm")
    MM_ke_M= MM / 1000
    print("Jadi, Jika", MM, "mm dikonversikan menjadi", MM_ke_M, "Meter" )
    print("\t=================================================================")
    back_to_MM()

def MM_ke_DM():
    print("========================================================================")
    print("|                   KONVERSI MILIMETER KE DESIMETER                    |")
    print("========================================================================")
    MM= float(input("Masukkan angka yang ingin di konversikan (mm) : "))
    print("Angka dalam milimeter adalah : ", MM, "mm")
    MM_ke_DM= MM / 100
    print("Jadi, Jika", MM, "mm dikonversikan menjadi", MM_ke_DM, "Desimeter" )
    print("\t=================================================================")
    back_to_MM()

def MM_ke_CM():
    print("========================================================================")
    print("|                   KONVERSI MILIMETER KE CENTIMETER                   |")
    print("========================================================================")
    MM= float(input("Masukkan angka yang ingin di konversikan (mm) : "))
    print("Angka dalam milimeter adalah : ", MM, "mm")
    MM_ke_CM= MM / 10
    print("Jadi, Jika", MM, "mm dikonversikan menjadi", MM_ke_CM, "Centimeter" )
    print("\t=================================================================")
    back_to_MM()

######################################## LOGOUT #####################################
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

######################################## ERROR ######################################
def error():
    print("========================================================================")
    print("|             UPS, TIDAK VALID! SILAHKAN MASUKKAN KEMBALI              |")
    print("========================================================================")

########################### JIKA ERROR INPUAN TIGA KALI #############################
def error_3():  
    print("========================================================================")
    print("|   UPS, ANDA SALAH MEMASUKKAN USERNAME DAN PASSWORD SEBANYAK 3 KALI   |")
    print("========================================================================")

################################3 TAMPILAN AWAL LOGIN ###############################
def login():
    clear()
    print("========================================================================")
    print("|                 SILAHKAN MASUKKAN USERNAME DAN PASSWORD              |")
    print("========================================================================")

############################### TAMPILAN AWAL POSTTEST 4 ############################
def posttest_4():
    print("========================================================================")
    print("|                             SELAMAT DATANG                           |")
    print("|                                   DI                                 |")
    print("|                      PROGRAM SEDERHANA POSTTEST 4                    |")
    print("|                                  OLEH                                |")
    print("|                      AGSEL FALANA SUPARLAN PUTRA                     |")
    print("========================================================================")
    print("|            Silahkan pilih apa yang akan anda konversikan             |")
    print("|                                !!!!!!!!                              |")
    print("| [1] Konversi Kilometer                                               |")
    print("| [2] Konversi Hektometer                                              |")
    print("| [3] Konversi Meter                                                   |")
    print("| [4] Konversi Desimeter                                               |")
    print("| [5] Konversi Centimeter                                              |")
    print("| [6] Konversi Milimeter                                               |")
    print("| [0] Kembali                                                          |")
    print("========================================================================")

##################################### PEMANGGILAN LOGIN ####################################
login()
nama = "agsel"
kunci = "apaya"
salah = 0
while True:
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    if username == nama and password == kunci :
            time.sleep(0.5)
            clear()
            while True:
                ######################## TAMPILAN AWAL PROGRAM POSTTEST 5 #######################
                print("========================================================================")
                print("|                             SELAMAT DATANG                           |")
                print("|                                   DI                                 |")
                print("|                      PROGRAM SEDERHANA POSTTEST 5                    |")
                print("|                                  OLEH                                |")
                print("|                      AGSEL FALANA SUPARLAN PUTRA                     |")
                print("========================================================================")
                print("| [1] Posttest 4                                                       |")
                print("| [0] Keluar Program                                                   |")
                print("========================================================================")
                pilihan_menu=int(input("Masukkan pilihan : "))
                ########################## PEMANGGILAN KONVERSI KM ##############################
                if pilihan_menu == 1:
                    clear()
                    time.sleep(0.5)
                    posttest_4()
                    pilihan_menu=int(input("Masukkan pilihan :"))
                    if pilihan_menu == 1 :
                        clear()
                        time.sleep(0.5)
                        konversi_KM()
                        pilihan_menu=int(input("Masukkan pilihan :"))
                        if pilihan_menu == 1 :
                            clear()
                            time.sleep(0.5)
                            KM_ke_HM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 2 :
                            clear()
                            time.sleep(0.5)
                            KM_ke_M()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 3 :
                            clear()
                            time.sleep(0.5)
                            KM_ke_DM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 4 :
                            clear()
                            time.sleep(0.5)
                            KM_ke_CM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 5 :
                            clear()
                            time.sleep(0.5)
                            KM_ke_MM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 0 :
                            clear()
                            time.sleep(0.5)
                            posttest_4()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        else:
                            error()
                            pilihan_menu-int(input("Masukkan Pilihan : "))
                            clear()
                            time.sleep(0.5)
                    
                ########################## PEMANGGILAN KONVERSI HM ##############################
                    elif pilihan_menu == 2 :
                        clear()
                        time.sleep(0.5)
                        konversi_HM()
                        pilihan_menu=int(input("Masukkan pilihan :"))
                        if pilihan_menu == 1 :
                            clear()
                            time.sleep(0.5)
                            HM_ke_KM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 2 :
                            clear()
                            time.sleep(0.5)
                            HM_ke_M()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 3 :
                            clear()
                            time.sleep(0.5)
                            HM_ke_DM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 4 :
                            clear()
                            time.sleep(0.5)
                            HM_ke_CM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 5 :
                            clear()
                            time.sleep(0.5)
                            HM_ke_MM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 0 :
                            clear()
                            time.sleep(0.5)
                            posttest_4()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        else:
                            error()
                            pilihan_menu-int(input("Masukkan Pilihan : "))
                            clear()
                            time.sleep(0.5)
                    
                ########################## PEMANGGILAN KONVERSI M ##############################
                    elif pilihan_menu == 3 :
                        clear()
                        time.sleep(0.5)
                        konversi_M()
                        pilihan_menu=int(input("Masukkan pilihan :"))
                        if pilihan_menu == 1 :
                            clear()
                            time.sleep(0.5)
                            M_ke_KM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 2 :
                            clear()
                            time.sleep(0.5)
                            M_ke_HM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 3 :
                            clear()
                            time.sleep(0.5)
                            M_ke_DM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 4 :
                            clear()
                            time.sleep(0.5)
                            M_KE_CM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 5 :
                            clear()
                            time.sleep(0.5)
                            M_KE_MM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 0 :
                            clear()
                            time.sleep(0.5)
                            posttest_4()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        else:
                            error()
                            pilihan_menu-int(input("Masukkan Pilihan : "))
                            clear()
                            time.sleep(0.5)
                    
                ########################## PEMANGGILAN KONVERSI DM ##############################
                    elif pilihan_menu == 4 :
                        clear()
                        time.sleep(0.5)
                        konversi_DM()
                        pilihan_menu=int(input("Masukkan pilihan :"))
                        if pilihan_menu == 1 :
                            clear()
                            time.sleep(0.5)
                            DM_ke_KM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 2 :
                            clear()
                            time.sleep(0.5)
                            DM_ke_HM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 3 :
                            clear()
                            time.sleep(0.5)
                            DM_ke_M()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 4 :
                            clear()
                            time.sleep(0.5)
                            DM_ke_CM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 5 :
                            clear()
                            time.sleep(0.5)
                            DM_ke_MM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 0 :
                            clear()
                            time.sleep(0.5)
                            posttest_4()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        else:
                            error()
                            pilihan_menu-int(input("Masukkan Pilihan : "))
                            clear()
                            time.sleep(0.5)
                    
                ########################## PEMANGGILAN KONVERSI CM ##############################
                    elif pilihan_menu == 5 :
                        clear()
                        time.sleep(0.5)
                        konversi_CM()
                        pilihan_menu=int(input("Masukkan pilihan :"))
                        if pilihan_menu == 1 :
                            clear()
                            time.sleep(0.5)
                            CM_ke_KM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 2 :
                            clear()
                            time.sleep(0.5)
                            CM_ke_HM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 3 :
                            clear()
                            time.sleep(0.5)
                            CM_ke_M()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 4 :
                            clear()
                            time.sleep(0.5)
                            CM_ke_DM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 5 :
                            clear()
                            time.sleep(0.5)
                            CM_ke_MM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 0 :
                            clear()
                            time.sleep(0.5)
                            posttest_4()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        else:
                            error()
                            pilihan_menu-int(input("Masukkan Pilihan : "))
                            clear()
                            time.sleep(0.5)
                    
                ########################## PEMANGGILAN KONVERSI MM ##############################
                    elif pilihan_menu == 6 :
                        clear()
                        time.sleep(0.5)
                        konversi_MM()
                        pilihan_menu=int(input("Masukkan pilihan :"))
                        if pilihan_menu == 1 :
                            clear()
                            time.sleep(0.5)
                            MM_ke_KM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 2 :
                            clear()
                            time.sleep(0.5)
                            MM_ke_HM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 3 :
                            clear()
                            time.sleep(0.5)
                            MM_ke_M()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 4 :
                            clear()
                            time.sleep(0.5)
                            MM_ke_DM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 5 :
                            clear()
                            time.sleep(0.5)
                            MM_ke_CM()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        elif pilihan_menu == 0 :
                            clear()
                            time.sleep(0.5)
                            posttest_4()
                            pilihan_menu=int(input("Masukkan pilihan :"))
                        else:
                            error()
                            pilihan_menu-int(input("Masukkan Pilihan : "))
                            clear()
                            time.sleep(0.5)
                
                ########################## PEMANGGILAN LOGOUT ##############################
                elif (pilihan_menu == 0):
                    clear()
                    time.sleep(0.5)
                    logout()  
                    exit()
                
                ########################## PEMANGGILAN JIKA SALAH INPUTAN ############################
                else:
                    clear()
                    time.sleep(0.5)
                    error()
                    time.sleep(0.5)
    
    ########################## JIKA TERDAPAT KESALAHAN SAAT LOGINA ##############################
    else :
          salah += 1
          time.sleep(0.5)
          print("========================================================================")
          print("| USERNAME ATAU PASSWORD YANG ANDA MASUKKAN SALAH SILAHKAN CEK KEMBALI |")
          print("========================================================================")
          if salah == 3 :
             print("========================================================================")
             print("|              UPS SORRY, ANDA SALAH SEBANYAK TIGA KALI!!!             |")
             print("========================================================================")
             break