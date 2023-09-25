# LOGIN SEDERHANA (NIM, NAMA, PASSWORD)
# MENGHITUNG BANGUN RUANG (BOLA, TABUNG, LIMAS SEGITIGA)
#2309116002_NYOMANARINITRIRAHAYU_SI_A


import math
import os
import sys

# Input data
akun={"Nama" : ["arini"],
      "NIM" : ["2309116002"],
      "Password" : ["123"]
      }
while True:
  Nama = input("Masukkan Nama :")
  NIM = input("Masukkan NIM :")
  Password = input("Masukkan Password :")

# Mengecek data 
  try:
    cariin = akun.get("Nama").index(Nama)
    if Nama == akun.get("Nama")[cariin] and NIM == akun.get("NIM")[cariin] and Password == akun.get("Password")[cariin]:
      print("login berhasil")
      def menu():
          print("""

===============| VOLUME BANGUN RUANG |====================        
PILIHAN BANGUN RUANG
Contoh : A untuk menghitung volume bola
  A. Volume Bola

  B. Volume Tabung

  C. Volume Limas Segitiga

  D. Keluar
===============| SELAMAT DATANG |==================== 
 """) 
      menu()
      while True :
        opp = input("Masukkan Pilihan Anda :")
        if opp == "A":
           print("Volume Bola")
           r = float(input("Masukkan jari jari : "))
           h = (4/3) * math.pi * r**3
           print(f"Volume bola: {h}")
        elif opp == "B":
           print("Volume Tabung")
           r = float(input("Masukkan jari-jari tabung: "))
           t = float(input("Masukkan tinggi tabung: "))
           h = math.pi * r**2 * t
           print(f"Volume tabung: {h}")
        elif opp == "C":
           print("Volume Limas Segitiga")
           a = float(input("Masukkan alas segitiga: "))
           t = float(input("Masukkan tinggi segitiga: "))
           h = (1/3) * a * t
           print(f"Volume limas segitiga: {h}")
        elif opp == "D" :
           print("SELESAI")
           os.system ("pause\n");
           sys.exit(1)
           break
        else :
            print (""" PILIHAN TIDAK DITEMUKAN
           """)
            break
            
      break
    else : print("login gagal, password anda salah")
  except ValueError:
    print("maaf username tidak tersedia")