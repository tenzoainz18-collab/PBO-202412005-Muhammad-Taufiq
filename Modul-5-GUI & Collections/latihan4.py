import tkinter as tk
from tkinter import messagebox

class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Masukkan Suhu (Celsius)")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Konversi", command=self.konversi)
        self.button.pack(pady=5)

        self.hasil = tk.Label(root, text="Hasil: -")
        self.hasil.pack(pady=10)

    def konversi(self):
        nilai = self.entry.get()

        if nilai == "":
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong")
            return
        try:
            c = float(nilai)
            f = (c * 9 / 5) + 32
            self.hasil.config(text="Hasil: %.2f Fahrenheit" % f)
        except:
            messagebox.showerror("Error", "Input harus angka")

if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
