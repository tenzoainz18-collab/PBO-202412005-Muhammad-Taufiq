import tkinter as tk
from tkinter import messagebox
class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi GUI Sederhana")
        self.root.geometry("300x220")

        # Label
        self.label = tk.Label(
            root,
            text="Masukkan Nama Anda",
            font=("Aril", 12)
        )
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Button tampilkan isi Entry
        self.button_tampil = tk.Button(
            root,
            text="Tampilkan",
            command=self.tampilkan_text
        )
        self.button_tampil.pack(pady=5)

        # Button hapus isi Entry
        self.button_hapus = tk.Button(
            root,
            text="Hapus",
            command=self.hapus_text
        )
        self.button_hapus.pack(pady=5)

    def tampilkan_text(self):
        isi = self.entry.get()
        if isi:
            messagebox.showinfo("Isi Entry", isi)
        else:
            messagebox.showwarning("Peringatan", "Entry masih kosong!")

    def hapus_text(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
