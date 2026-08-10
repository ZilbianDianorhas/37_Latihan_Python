# Program Pengecekan Ganjil / Genap

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"


while True:
    print("\n=== PROGRAM PENGECEKAN GANJIL / GENAP ===")

    angka = int(input("Masukkan sebuah angka: "))

    hasil = cek_ganjil_genap(angka)
    print(angka, "adalah", hasil)

    lanjut = input("Apakah ingin mengecek angka lagi? (y/n): ")

    if lanjut.lower() == "n":
        print("Program selesai.")
        break
    elif lanjut.lower() == "y":
        print("Silakan masukkan angka lagi.")
    else:
        print("Pilihan tidak valid, program akan lanjut.")