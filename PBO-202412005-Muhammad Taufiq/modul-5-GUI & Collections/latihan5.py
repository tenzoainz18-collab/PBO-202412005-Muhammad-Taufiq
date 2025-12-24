import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
# b. Class Tugas
class Tugas:
    def __init__(self, judul, status=False):
        self.judul = judul
        self.status = status  # False = belum selesai, True = selesai

    def status_text(self):
        return "Selesai" if self.status else "Belum Selesai"
# a. Aplikasi GUI
class AplikasiToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas")
        self.root.geometry("600x400")

        # List of objects
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul Tugas:").grid(row=0, column=0)
        self.entry_judul = tk.Entry(frame_input, width=40)
        self.entry_judul.grid(row=0, column=1, padx=5)

        tk.Button(
            frame_input,
            text="Tambah Tugas",
            command=self.tambah_tugas
        ).grid(row=0, column=2, padx=5)

        # Frame tombol
        frame_btn = tk.Frame(root, pady=10)
        frame_btn.pack()

        tk.Button(frame_btn, text="Edit", command=self.edit_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Hapus", command=self.hapus_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Tandai Selesai", command=self.tandai_selesai)\
            .pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(
            root,
            columns=("Judul", "Status"),
            show="headings"
        )
        self.tree.heading("Judul", text="Judul Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def tambah_tugas(self):
        judul = self.entry_judul.get()
        if judul == "":
            messagebox.showwarning("Peringatan", "Judul tugas tidak boleh kosong!")
            return
        tugas = Tugas(judul)
        self.daftar_tugas.append(tugas)

        self.tree.insert("", tk.END, values=(tugas.judul, tugas.status_text()))
        self.entry_judul.delete(0, tk.END)
        
    def hapus_tugas(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih tugas!")
            return

        index = self.tree.index(selected[0])
        del self.daftar_tugas[index]
        self.tree.delete(selected[0])

    def edit_tugas(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih tugas!")
            return
        index = self.tree.index(selected[0])
        tugas = self.daftar_tugas[index]
        
        judul_baru = simpledialog.askstring(
            "Edit Tugas",
            "Judul baru:",
            initialvalue=tugas.judul
        )
        if judul_baru:
            tugas.judul = judul_baru
            self.tree.item(
                selected[0],
                values=(tugas.judul, tugas.status_text())
            )
    def tandai_selesai(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih tugas!")
            return

        index = self.tree.index(selected[0])
        tugas = self.daftar_tugas[index]
        tugas.status = True

        self.tree.item(
            selected[0],
            values=(tugas.judul, tugas.status_text())
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiToDo(root)
    root.mainloop()
