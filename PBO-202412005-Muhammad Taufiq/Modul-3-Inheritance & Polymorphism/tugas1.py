class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} - Gaji Pokok: {self.gaji_pokok}"

# Child Class Manager
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager {self.nama} - Total Gaji: {total}"

# Child Class Programmer
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer {self.nama} - Total Gaji: {total}"

# Composition
class Departemen:
    def __init__(self, nama_dept):
        self.nama_dept = nama_dept
        self.daftar_karyawan = []  # list of objects

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar Karyawan di Departemen {self.nama_dept}:")
        for k in self.daftar_karyawan:
            print(" -", k.info_gaji())

# ======================
# Instansiasi
# ======================
# 2 Manager
m1 = Manager("Jalil", 7000000, 3000000)
m2 = Manager("Abrar", 6500000, 2500000)

# 2 Programmer
p1 = Programmer("Ariel", 5000000, 1500000)
p2 = Programmer("Cakra", 5500000, 2000000)

# Buat departemen
dept = Departemen("IT")

# Tambahkan semua karyawan
dept.tambah_karyawan(m1)
dept.tambah_karyawan(m2)
dept.tambah_karyawan(p1)
dept.tambah_karyawan(p2)

# Tampilkan semua info gaji
dept.tampilkan_karyawan()