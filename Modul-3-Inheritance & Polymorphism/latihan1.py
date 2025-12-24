# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Person: Nama = {self.nama}, Umur = {self.umur}"


# Class Mahasiswa (Inheritance dari Person)
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        # Memanggil constructor parent class
        super().__init__(nama, umur)
        self.nim = nim
    
    def info(self):
        return f"Mahasiswa: Nama = {self.nama}, Umur = {self.umur}, NIM = {self.nim}"

# Instansiasi objek
p = Person("Abrar", 22)
m = Mahasiswa("Ariel", 23, "123456789")

# Memanggil method info()
print(p.info())
print(m.info())