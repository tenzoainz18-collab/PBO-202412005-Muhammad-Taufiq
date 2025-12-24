import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} | {self.nama} | {self.jurusan} | {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru

class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Mahasiswa")
        self.root.geometry("800x500")

        # Dictionary of objects
        self.data_mahasiswa = {}

        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=1, column=0)
        tk.Label(frame_input, text="Jurusan").grid(row=2, column=0)
        tk.Label(frame_input, text="IPK").grid(row=3, column=0)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1)
        self.entry_nama.grid(row=1, column=1)
        self.entry_jurusan.grid(row=2, column=1)
        self.entry_ipk.grid(row=3, column=1)

        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=5)

        tk.Button(frame_btn, text="Tambah", command=self.tambah).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Update IPK", command=self.update_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Hapus", command=self.hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Cari", command=self.cari).pack(side=tk.LEFT, padx=5)

        # -------------------------
        # TREEVIEW
        # -------------------------
        self.tree = ttk.Treeview(
            root,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # -------------------------
        # FITUR TAMBAHAN
        # -------------------------
        frame_extra = tk.Frame(root)
        frame_extra.pack(pady=5)

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export TXT", command=self.export_txt).pack(side=tk.LEFT, padx=5)
        
        # ===== FILTER JURUSAN (3.e) =====
        frame_filter = tk.Frame(self.root)
        frame_filter.pack(pady=5)
        tk.Label(frame_filter, text="Filter Jurusan:").pack(side=tk.LEFT)
        self.combo_jurusan = ttk.Combobox(
            
        frame_filter,
        values=["Semua", "Informatika", "Sistem Informasi", "Teknik Komputer"],
        state="readonly"
        )
        self.combo_jurusan.current(0)
        self.combo_jurusan.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
        frame_filter,
        text="Filter",
        command=self.filter_jurusan
        ).pack(side=tk.LEFT)

    # =========================
    # VALIDASI INPUT
    # =========================
    def validasi(self, nim, nama, jurusan, ipk):
        if nim == "" or nama == "" or jurusan == "" or ipk == "":
            messagebox.showwarning("Error", "Semua field harus diisi")
            return False
        try:
            ipk = float(ipk)
            if ipk < 0 or ipk > 4:
                raise ValueError
        except:
            messagebox.showerror("Error", "IPK harus angka 0 - 4")
            return False
        return True

    # =========================
    # CRUD METHODS
    # =========================
    def filter_jurusan(self):
        jurusan = self.combo_jurusan.get()
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            if jurusan == "Semua" or mhs.jurusan == jurusan:
                self.tree.insert("",
                tk.END,
                values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk)
            )

    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk = self.entry_ipk.get()

        if not self.validasi(nim, nama, jurusan, ipk):
            return

        if nim in self.data_mahasiswa:
            messagebox.showerror("Error", "NIM sudah ada")
            return

        mhs = Mahasiswa(nim, nama, jurusan, float(ipk))
        self.data_mahasiswa[nim] = mhs
        self.refresh_tree()

    def hapus(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Error", "Pilih data")
            return
        nim = self.tree.item(selected[0])["values"][0]
        del self.data_mahasiswa[nim]
        self.refresh_tree()

    def update_ipk(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Error", "Pilih data")
            return
        nim = self.tree.item(selected[0])["values"][0]
        ipk_baru = self.entry_ipk.get()

        try:
            ipk_baru = float(ipk_baru)
            self.data_mahasiswa[nim].update_ipk(ipk_baru)
            self.refresh_tree()
        except:
            messagebox.showerror("Error", "IPK tidak valid")

    def cari(self):
        keyword = self.entry_nama.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nama.lower() or keyword in mhs.nim.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    # =========================
    # FITUR TAMBAHAN
    # =========================
    def rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"{rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return
        mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi", mhs.info())

    def export_txt(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file:
            return
        with open(file, "w") as f:
            for mhs in self.data_mahasiswa.values():
                f.write(mhs.info() + "\n")
        messagebox.showinfo("Sukses", "Data berhasil diekspor")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()