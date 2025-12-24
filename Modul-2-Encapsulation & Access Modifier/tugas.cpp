#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Buku {
public:
    string judul;
    string penulis;
    string kode_buku;
protected:
    int stok;              // protected
private:
    string lokasi_rak;     // private
public:
    Buku(string j, string p, string k, int s, string rak)
        : judul(j), penulis(p), kode_buku(k), stok(s), lokasi_rak(rak) {}
    // Getter lokasi rak
    string getLokasiRak() {
        return lokasi_rak;
    }
    // Setter lokasi rak
    void setLokasiRak(string rak) {
        lokasi_rak = rak;
    }
    // Tambah stok
    void tambahStok(int jumlah) {
        stok += jumlah;
    }
    // Kurangi stok
    bool kurangiStok(int jumlah) {
        if (stok >= jumlah) {
            stok -= jumlah;
            return true;
        }
        return false;
    }
    void infoBuku() {
        cout << judul << " | " << penulis 
             << " | Stok: " << stok 
             << " | Rak: " << lokasi_rak << endl;
    }
};

class Peminjaman {
public:
    string kode_buku;
    string tanggal_pinjam;
    string tanggal_kembali;
    string status;

    Peminjaman(string kode, string pinjam, string kembali = "-", string st = "Dipinjam")
        : kode_buku(kode), tanggal_pinjam(pinjam), tanggal_kembali(kembali), status(st) {}

    void infoPeminjaman() {
        cout << "Kode Buku: " << kode_buku
             << ", Pinjam: " << tanggal_pinjam
             << ", Kembali: " << tanggal_kembali
             << ", Status: " << status << endl;
    }
};

class Anggota {
public:
    string id_anggota;
    string nama;

protected:
    int maks_pinjam;        // protected

private:
    bool status_aktif;      // private

public:
    vector<Peminjaman> daftar_peminjaman;     // aggregation

    Anggota(string id, string n, int m, bool aktif = true)
        : id_anggota(id), nama(n), maks_pinjam(m), status_aktif(aktif) {}

    // Getter status
    bool getStatus() {
        return status_aktif;
    }

    // Setter status
    void setStatus(bool s) {
        status_aktif = s;
    }

    // Pinjam buku
    void pinjamBuku(Buku &buku, string tanggal) {
        if (!status_aktif) {
            cout << nama << " tidak aktif!" << endl;
            return;
        }

        if ((int)daftar_peminjaman.size() >= maks_pinjam) {
            cout << nama << " sudah mencapai batas maksimal peminjaman!" << endl;
            return;
        }

        if (buku.kurangiStok(1)) {
            daftar_peminjaman.push_back(Peminjaman(buku.kode_buku, tanggal));
            cout << nama << " berhasil meminjam " << buku.judul << endl;
        } else {
            cout << "Stok buku " << buku.judul << " habis!" << endl;
        }
    }

    // Kembalikan buku
    void kembalikanBuku(Buku &buku, string tanggal) {
        for (auto &p : daftar_peminjaman) {
            if (p.kode_buku == buku.kode_buku && p.status == "Dipinjam") {
                p.status = "Dikembalikan";
                p.tanggal_kembali = tanggal;
                buku.tambahStok(1);
                cout << nama << " mengembalikan " << buku.judul << endl;
                return;
            }
        }
        cout << "Buku tidak ditemukan dalam daftar peminjaman!" << endl;
    }

    void infoAnggota() {
        cout << "ID: " << id_anggota 
             << " | Nama: " << nama 
             << " | Status: " << (status_aktif ? "Aktif" : "Nonaktif") 
             << endl;
    }
};

class Perpustakaan {
public:
    vector<Buku*> daftar_buku;  // composition (mengelola objek Buku)

    void tambahBuku(Buku* b) {
        daftar_buku.push_back(b);
    }

    void infoBuku() {
        for (auto b : daftar_buku) {
            b->infoBuku();
        }
    }
};

int main() {

    Perpustakaan perpus;

    // 3 Buku
    Buku* b1 = new Buku("Python Dasar", "Abrar", "B001", 3, "Rak A1");
    Buku* b2 = new Buku("Pemrograman Dasar", "ariel", "B002", 2, "Rak A2");
    Buku* b3 = new Buku("Database SQL", "Cakra", "B003", 1, "Rak A3");

    perpus.tambahBuku(b1);
    perpus.tambahBuku(b2);
    perpus.tambahBuku(b3);

    // 2 Anggota
    Anggota a1("A01", "Abrar", 3);
    Anggota a2("A02", "Ariel", 2);

    // Peminjaman
    a1.pinjamBuku(*b1, "2025-01-01");
    a1.pinjamBuku(*b2, "2025-01-01");
    a2.pinjamBuku(*b3, "2025-01-02");

    // Pengembalian
    a1.kembalikanBuku(*b1, "2025-01-05");

    cout << "\n==============================\n";
    cout << "       INFORMASI BUKU\n";
    cout << "==============================\n";
    perpus.infoBuku();

    cout << "\n==============================\n";
    cout << "       INFORMASI ANGGOTA\n";
    cout << "==============================\n";
    a1.infoAnggota();
    a2.infoAnggota();

    cout << "\n==============================\n";
    cout << " DAFTAR PEMINJAMAN ANGGOTA 1\n";
    cout << "==============================\n";
    for (auto &p : a1.daftar_peminjaman) {
        p.infoPeminjaman();
    }

    cout << "\n==============================\n";
    cout << " DAFTAR PEMINJAMAN ANGGOTA 2\n";
    cout << "==============================\n";
    for (auto &p : a2.daftar_peminjaman) {
        p.infoPeminjaman();
    }

    return 0;
}
