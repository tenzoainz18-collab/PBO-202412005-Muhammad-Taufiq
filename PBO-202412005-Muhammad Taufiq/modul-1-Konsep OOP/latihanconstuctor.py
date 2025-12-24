class Kendaraan:

    Bahanbakar = "Pertalite"

# Constructor
    def __init__(self, Merek, Warna, tahun):
# Instance attributes
        self.Merek = Merek
        self.Warna = Warna
        self.tahun = tahun

    def info_Kendaraan(self):
        return f"Kendaraan {self.Merek} oleh {self.Warna} ({self.tahun})"

# Instansiasi object
mobil1 = Kendaraan("HRV", "Hitam", 2021)
mobil2 = Kendaraan("TOYOTA", "Merah", 2023)

print(mobil1.info_Kendaraan())
print(mobil2.info_Kendaraan())
print(f"Bahanbakar: {Kendaraan.Bahanbakar}")