#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ===========================
// CLASS BUKU
// ===========================
class Buku {
public:
    string judul, penulis, kode_buku;

protected:
    int stok;

private:
    string lokasi_rak;

public:
    Buku(string j, string p, string k, int s, string rak)
        : judul(j), penulis(p), kode_buku(k), stok(s), lokasi_rak(rak) {}

    string getLokasiRak() { return lokasi_rak; }
    void setLokasiRak(string rak) { lokasi_rak = rak; }

    bool kurangiStok() {
        if (stok > 0) { stok--; return true; }
        return false;
    }

    void tambahStok() { stok++; }

    void infoBuku() {
        cout << judul << " | " << penulis 
             << " | Stok: " << stok 
             << " | Rak: " << lokasi_rak << endl;
    }
};

// ===========================
// CLASS PEMINJAMAN
// ===========================
class Peminjaman {
public:
    string kode_buku, tanggal_pinjam, tanggal_kembali, status;

    Peminjaman(string kode, string pinjam)
        : kode_buku(kode), tanggal_pinjam(pinjam), tanggal_kembali("-"), status("Dipinjam") {}

    void infoPeminjaman() {
        cout << "Kode: " << kode_buku 
             << ", Pinjam: " << tanggal_pinjam
             << ", Kembali: " << tanggal_kembali
             << ", Status: " << status << endl;
    }
};

// ===========================
// CLASS ANGGOTA
// ===========================
class Anggota {
public:
    string id_anggota, nama;

protected:
    int maks_pinjam;

private:
    bool status_aktif;

public:
    vector<Peminjaman> daftar_peminjaman;

    Anggota(string id, string n, int maks)
        : id_anggota(id), nama(n), maks_pinjam(maks), status_aktif(true) {}

    void pinjamBuku(Buku &b, string tanggal) {
        if (!status_aktif) { cout << nama << " tidak aktif!\n"; return; }
        if (daftar_peminjaman.size() >= maks_pinjam) { 
            cout << "Batas pinjam tercapai!\n"; return; 
        }

        if (b.kurangiStok()) {
            daftar_peminjaman.push_back(Peminjaman(b.kode_buku, tanggal));
            cout << nama << " meminjam " << b.judul << endl;
        } else {
            cout << "Stok buku habis!\n";
        }
    }

    void kembalikanBuku(Buku &b, string tanggal) {
        for (auto &p : daftar_peminjaman) {
            if (p.kode_buku == b.kode_buku && p.status == "Dipinjam") {
                p.status = "Dikembalikan";
                p.tanggal_kembali = tanggal;
                b.tambahStok();
                cout << nama << " mengembalikan " << b.judul << endl;
                return;
            }
        }
        cout << "Tidak ditemukan dalam daftar peminjaman!\n";
    }
};

// ===========================
// CLASS PERPUSTAKAAN (COMPOSITION)
// ===========================
class Perpustakaan {
public:
    vector<Buku*> daftar_buku;

    void tambahBuku(Buku *b) { daftar_buku.push_back(b); }

    void infoBuku() {
        for (auto b : daftar_buku) b->infoBuku();
    }
};

// ===========================
// MAIN PROGRAM
// ===========================
int main() {

    Perpustakaan perpus;

    // 3 buku
    Buku b1("Python Dasar", "Andi", "B001", 3, "Rak A1");
    Buku b2("Java", "Budi", "B002", 2, "Rak A2");
    Buku b3("SQL Database", "Citra", "B003", 1, "Rak A3");

    perpus.tambahBuku(&b1);
    perpus.tambahBuku(&b2);
    perpus.tambahBuku(&b3);

    // 2 anggota
    Anggota a1("A01", "Rina", 3);
    Anggota a2("A02", "Doni", 2);

    // Peminjaman
    a1.pinjamBuku(b1, "2025-01-01");
    a1.pinjamBuku(b2, "2025-01-01");

    a2.pinjamBuku(b3, "2025-01-02");

    // Pengembalian
    a1.kembalikanBuku(b1, "2025-01-05");

    // ================================
    cout << "\n=== INFORMASI BUKU ===\n";
    perpus.infoBuku();

    cout << "\n=== ANGGOTA 1 ===\n";
    for (auto &p : a1.daftar_peminjaman) p.infoPeminjaman();

    cout << "\n=== ANGGOTA 2 ===\n";
    for (auto &p : a2.daftar_peminjaman) p.infoPeminjaman();

    return 0;
}
