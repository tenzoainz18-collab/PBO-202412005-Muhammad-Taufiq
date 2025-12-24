class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []   

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        total = sum(n.skor for n in self.daftar_nilai)
        return round(total / len(self.daftar_nilai), 2)

class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []   

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)

class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []  

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

if __name__ == "__main__":
    uni = Universitas("Universitas A")

    prodi1 = uni.buat_program("Teknik Informatika")
    prodi2 = uni.buat_program("Bisnis Digital")
    prodi3 = uni.buat_program("Teknik Elektro")

    mk1 = MataKuliah("TI01", "Pemrograman Dasar")
    mk2 = MataKuliah("TI02", "Struktur Data")
    prodi1.tambah_matakuliah(mk1)
    prodi1.tambah_matakuliah(mk2)

    mk3 = MataKuliah("Bisdig01", "Analisis Sistem")
    mk4 = MataKuliah("Bisdig02", "Basis Data")
    prodi2.tambah_matakuliah(mk3)
    prodi2.tambah_matakuliah(mk4)

    mk5 = MataKuliah("TE01", "Elektronika")
    mk6 = MataKuliah("TE02", "Sistem Digital")
    prodi3.tambah_matakuliah(mk5)
    prodi3.tambah_matakuliah(mk6)

    m1 = Mahasiswa("23001", "Herman")
    m2 = Mahasiswa("23002", "Abror")
    m3 = Mahasiswa("23003", "Riel")

    m1.tambah_nilai(Nilai("TI01", 85))
    m1.tambah_nilai(Nilai("TI02", 90))

    m2.tambah_nilai(Nilai("Bisdig201", 78))
    m2.tambah_nilai(Nilai("Bisdig02", 88))

    m3.tambah_nilai(Nilai("TE01", 70))
    m3.tambah_nilai(Nilai("TE02", 95))

    def tampil_mk(prodi: ProgramStudi):
        print(f"\nDaftar MK {prodi.nama}:")
        for mk in prodi.daftar_matakuliah:
            print(f"- {mk.kode} : {mk.nama}")

    tampil_mk(prodi1)
    tampil_mk(prodi2)
    tampil_mk(prodi3)

    def tampil_nilai(m: Mahasiswa):
        print(f"\nNilai {m.nama}:")
        for n in m.daftar_nilai:
            print(f"- {n.kode_mk} : {n.skor}")

    tampil_nilai(m1)
    tampil_nilai(m2)
    tampil_nilai(m3)

    print("\nRata-rata Nilai Mahasiswa:")
    print(f"{m1.nama}: {m1.rata_rata()}")
    print(f"{m2.nama}: {m2.rata_rata()}")
    print(f"{m3.nama}: {m3.rata_rata()}")

    def report_program(prodi: ProgramStudi, semua_mahasiswa):
        print("\n" + "=" * 40)
        print(f"Report Program Studi: {prodi.nama}")
        print("Mata Kuliah:", ", ".join(mk.kode for mk in prodi.daftar_matakuliah))

        for m in semua_mahasiswa:
            relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
            if relevan:
                avg = sum(n.skor for n in relevan) / len(relevan)
                print(f"{m.nama}: {round(avg, 2)}")

    report_program(prodi1, [m1, m2, m3])
    report_program(prodi2, [m1, m2, m3])
    report_program(prodi3, [m1, m2, m3])

