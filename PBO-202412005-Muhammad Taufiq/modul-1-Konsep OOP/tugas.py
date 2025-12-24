class Mahasiswa:
    
    universitas = "STITEK Bontang"
    
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # 2.a. Instance Attributes: 
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    #Method Perkenalan Diri
    def perkenalan_diri(self):
        return (f"Halo, saya {self.nama} ({self.nim}) dari Jurusan {self.jurusan}. "
        f"Saya adalah mahasiswa di **{Mahasiswa.universitas}** dengan IPK saat ini {self.ipk:.2f}.")

    # Method Update IPK
    def update_ipk(self, ipk_baru):
        """Memperbarui nilai IPK mahasiswa."""
        try:
            ipk_baru = float(ipk_baru)
            if 0.0 <= ipk_baru <= 4.0:
                self.ipk = ipk_baru
                return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk:.2f}."
            else:
                return "Pembaruan gagal: Nilai IPK harus antara 0.0 hingga 4.0."
        except ValueError:
            return "Pembaruan gagal: IPK baru harus berupa angka."

    # Method Predikat Kelulusan
    def predikat_kelulusan(self):
        """Menentukan predikat kelulusan berdasarkan IPK."""
        ipk = self.ipk
        
        if ipk >= 3.5:
            predikat = "Cum Laude"
        elif ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif ipk >= 2.5:
            predikat = "Memuaskan"
        elif ipk >= 2.0:
            predikat = "Lulus"
        else:
            predikat = "Belum Lulus / IPK di bawah standar kelulusan (2.0)"
            
        return f"Predikat kelulusan yang mungkin dicapai adalah: **{predikat}**."

# Instansiasi 3 objek Mahasiswa
mhs1 = Mahasiswa("Muhammad Ruwaifih Abrar", "202412024", "Teknik Informatika", ipk=3.90)
mhs2 = Mahasiswa("Ariel Agnibrata Rufit", "202412026", "Teknik Informatika", ipk=3.85)
mhs3 = Mahasiswa("Muhammad Taufiq", "202412005", "Teknik Informatika", ipk=2.80)

print("- INFORMASI AWAL MAHASISWA -")
print(mhs1.perkenalan_diri())
print(mhs2.perkenalan_diri())
print(mhs3.perkenalan_diri())

print("\n - Update IPK -")
print(mhs1.update_ipk(3.90))
print(mhs1.perkenalan_diri())

# 2. Cek predikat kelulusan
print("\n- DEMONSTRASI PREDIKAT KELULUSAN -")
print(f"{mhs1.nama}: {mhs1.predikat_kelulusan()}")
print(f"{mhs2.nama}: {mhs2.predikat_kelulusan()}")
print(f"{mhs3.nama}: {mhs3.predikat_kelulusan()}")
