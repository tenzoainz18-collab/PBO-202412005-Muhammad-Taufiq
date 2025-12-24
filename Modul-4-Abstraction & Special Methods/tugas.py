from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass

class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        print(f"{self.nama} memiliki hak akses member.")

    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)

class PoinTidakValidError(Exception):
    def __init__(self, pesan):
        super().__init__(pesan)

def input_poin(prompt):
    nilai = input(prompt)

    if nilai.strip() == "":
        raise ValueError("Input tidak boleh kosong!")

    try:
        nilai = int(nilai)
    except:
        raise ValueError("Input harus berupa angka!")

    if nilai < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")

    return nilai

print("=== Input Data Member ===")
try:
    nama1 = input("Masukkan nama Member 1: ")
    p1 = input_poin("Masukkan poin Member 1: ")

    nama2 = input("Masukkan nama Member 2: ")
    p2 = input_poin("Masukkan poin Member 2: ")

    # Membuat objek
    m1 = Member(nama1, p1)
    m2 = Member(nama2, p2)

    print("\n=== Output ===")
    print("Info Member 1:", m1)
    print("Info Member 2:", m2)

    print("Jumlah poin (m1 + m2):", m1 + m2)
    print("Panjang nama member 1 (len(m1)):", len(m1))

    print("\nHak akses:")
    m1.akses()
    m2.akses()

    # Uji masukan negatif
    print("\n=== Uji Exception Negatif ===")
    input_poin("Masukkan poin negatif untuk uji error: ")

except ValueError as ve:
    print("ValueError:", ve)
except PoinTidakValidError as pe:
    print("Custom Error:", pe)
except Exception as e:
    print("Error lainnya:", e)
