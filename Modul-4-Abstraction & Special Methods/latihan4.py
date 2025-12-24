class UmurTidakValidError(Exception):
    """Kesalahan umum untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(UmurTidakValidError):
    """Error jika umur terlalu muda (< 5)."""
    pass

class UmurTerlaluTuaError(UmurTidakValidError):
    """Error jika umur terlalu tua (> 100)."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Error jika umur tidak memenuhi syarat pembuatan akun."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimum 100 tahun.")
    return umur

def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya boleh dibuat untuk umur 18 tahun ke atas!")
    return "Akun berhasil dibuat!"

if __name__ == "__main__":

    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)   # validasi umur lengkap
            break                # keluar jika umur valid

        except ValueError:
            print("Input harus berupa bilangan bulat!")

        except UmurTerlaluMudaError as e:
            print("Error:", e)

        except UmurTerlaluTuaError as e:
            print("Error:", e)

        except UmurTidakValidError as e:
            print("Error:", e)

        except Exception as e:
            print("Kesalahan tidak dikenal:", e)

        print("Silakan coba lagi.\n")

    print("\nUmur valid tersimpan:", umur)

    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print("Gagal membuat akun:", e)