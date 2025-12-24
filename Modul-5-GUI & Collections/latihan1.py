class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} | {self.penulis} | {self.tahun}"

daftar_buku = [
    Buku("Pemrograman Python", "Abrar", 2020),
    Buku("Basis Data", "Aril", 2019),
    Buku("Algoritma", "Abrar", 2018),
    Buku("Struktur Data", "Cakra", 2021),
    Buku("OOP Python", "Abrar", 2022)
]
def cari_buku_berdasarkan_penulis(list_buku, nama_penulis):
    hasil = []
    for buku in list_buku:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil

penulis_dicari = "Abrar"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print(f"=== Buku karya {penulis_dicari} ===")
if hasil_pencarian:
    for buku in hasil_pencarian:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")
