class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.nama} - {self.email}"

data_pelanggan = {}

#Fungsi menambah pelanggan
def tambah_pelanggan(pelanggan):
    data_pelanggan[pelanggan.id_pelanggan] = pelanggan

# Fungsi menghapus pelanggan
def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print(f"Pelanggan {id_pelanggan} berhasil dihapus")
    else:
        print("Pelanggan tidak ditemukan")

# Fungsi mencari pelanggan
def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None

# Menambahkan data pelanggan
tambah_pelanggan(Pelanggan("PL001", "Abrar", "abrar@email.com"))
tambah_pelanggan(Pelanggan("PL002", "Cakra", "Cakra@email.com"))
tambah_pelanggan(Pelanggan("PL003", "Ariel", "Ariel@email.com"))

print("=== Daftar Pelanggan ===")
for id_pel, pelanggan in data_pelanggan.items():
    print(f"{id_pel}: {pelanggan.info()}")

# Mencari pelanggan
id_cari = "PL002"
hasil = cari_pelanggan(id_cari)
if hasil:
    print(f"\nPelanggan ditemukan: {hasil.info()}")
else:
    print("\nPelanggan tidak ditemukan")
