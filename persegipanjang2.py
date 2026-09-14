# Fungsi untuk menghitung luas persegi panjang
def hitung_luas(panjang, lebar):
    return panjang * lebar

# Input dari pengguna
panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))

# Memanggil fungsi
luas = hitung_luas(panjang, lebar)

# Menampilkan hasil
print(f"Luas persegi panjang adalah {luas}")