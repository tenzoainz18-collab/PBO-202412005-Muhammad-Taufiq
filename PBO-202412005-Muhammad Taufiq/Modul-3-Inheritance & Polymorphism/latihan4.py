class Penulis:
    def __init__(self, nama):
        self.nama = nama
    def info(self):
        return f"Penulis: {self.nama}"

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis   # Composition

    def info(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"

# Instansiasi
p = Penulis("Tere Liye")
b = Buku("Bumi", p)

print(b.info())
print("Nama penulis dari objek buku:", b.penulis.nama)