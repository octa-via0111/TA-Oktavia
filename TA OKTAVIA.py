import tkinter as tk
from tkinter import messagebox, ttk
from collections import deque  # implementasi queue

class Item:
    def __init__(self, kode_barang, nama_barang, deskripsi, jumlah_stok, harga_per_unit, pemasok):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.deskripsi = deskripsi
        self.jumlah_stok = jumlah_stok
        self.harga_per_unit = harga_per_unit
        self.pemasok = pemasok

    def status(self):
        return "Tersedia" if self.jumlah_stok > 0 else "Tidak Tersedia"

class InventarisManager:
    def __init__(self):
        self.items = []
        self.queue = deque()  # menyimpan item yang dihapus

    def tambah_item(self, item):
        self.items.append(item)

    def tampilkan_inventaris(self):
        return [(item.kode_barang, item.nama_barang,
                 item.deskripsi, item.jumlah_stok,
                 item.harga_per_unit, item.status(), item.pemasok) for item in self.items]

    def hapus_item(self, kode_barang):
        for i in range(len(self.items)):
            if self.items[i].kode_barang == kode_barang:
                item_hapus = self.items.pop(i)  # Menghapus item
                self.queue.append(item_hapus)  # Menyimpan item yang dihapus ke queue
                return True
        return False

    def tampilkan_queue(self):
        return [(item.kode_barang, item.nama_barang, item.deskripsi) for item in self.queue]

# Fungsi menambah item dari input pengguna
def tambah_item():
    selected_index = combo_item.current()
    
    if selected_index == -1:
        messagebox.showerror("Error", "Pilih barang dari daftar.")
        return
    
    kode_barang = kode_barang_list[selected_index]
    nama_barang = nama_barang_list[selected_index]
    deskripsi = combo_deskripsi.get()
    
    jumlah_stok = stok_list[selected_index]
    harga_per_unit = harga_list[selected_index]
    pemasok = pemasok_list[selected_index]

    item_baru = Item(kode_barang, nama_barang, deskripsi, jumlah_stok, harga_per_unit, pemasok)
    inventaris_manager.tambah_item(item_baru)
    
    messagebox.showinfo("Info", "Item berhasil ditambahkan!")
    show_inventaris()

# Fungsi menghapus item berdasarkan kode barang
def hapus_item():
    kode_brg = entry_delete_code.get()   
    if not kode_brg:
        messagebox.showerror("Error", "Masukkan kode barang untuk dihapus.")
        return
    
    if inventaris_manager.hapus_item(kode_brg):
        messagebox.showinfo("Info", "Item berhasil dihapus!")
        entry_delete_code.delete(0, tk.END)
        show_inventaris()
        show_queue()
    else:
        messagebox.showerror("Error", "Item tidak ditemukan!")

# Fungsi menampilkan inventaris dalam Treeview
def show_inventaris():
    for item in tree_inventaris.get_children():
        tree_inventaris.delete(item)
    
    for item in inventaris_manager.tampilkan_inventaris():
        tree_inventaris.insert("", "end", values=item)

# Fungsi menampilkan item yang dihapus dalam queue
def show_queue():
    for item in tree_queue.get_children():
        tree_queue.delete(item)
    
    for item in inventaris_manager.tampilkan_queue():
        tree_queue.insert("", "end", values=item)

inventaris_manager = InventarisManager()

root = tk.Tk()
root.title('Inventaris Butik')
root.geometry("900x600")
root.configure(bg='lightblue')

# Tambahkan nama butik di bagian atas jendela
tk.Label(root, text="~BOUTIQU~", font=("Felix Titling", 30, "bold"), bg='lightblue').pack(pady=10)

# Daftar barang dan atributnya
kode_barang_list = ['1020', '1021', '1022', '1023', '1024', '1026', '1027', '1028', '1111', '1112', 
                    '1113', '1114', '1115', '2001', '2002', '2003', '2004', '2005', '2006', '2030', 
                    '2031', '2032', '2033', '2034', '2035', '2121', '2122', '2123', '2124', '2125']
nama_barang_list = ['Kemeja', 'Kaca Mata', 'Dress', 'Pant', 'Blazer', 'Cardigan', 'Aksesoris Modis', 
                    'Blous', 'Pyjamas', 'Kebaya', 'Rok']
deskripsi_list = ['Maxi Dress', 'Kimono Dress', 'Wrap Dress', 'Ruffle Dress', 'Panjang', 'Wide Leg Pants', 
                  'Straight Pants', 'Abstrak', 'Flowers', 'Kotak Korea', 'Slim Fit Jeans', 'Kebaya Kutubaru', 
                  'Kebaya Encim', 'Kebaya Sunda', 'Kebaya Bali', 'Ankle pants', 'Pegged Pants', 'Kulot pants', 
                  'Sheat Dress', 'Knits Over Dresses', 'Lensa Minus', 'Syal', 'Blazer Denim', 'Jas Blazer', 
                  'Boyfriend Blazer', 'Draped Blazer', 'Corak Bintik', 'Anting', 'Lengan Pendek', 'Puff Sleeve Blouse', 
                  'Fitted Blazer', 'Kebaya Modern', 'Jeans', 'Motif Tradisional', 'Classic Cardigans', 'Hoodie Cardigan', 
                  'Vest Cardigan ', 'Belted Cardigan', 'Long Cardigan', 'Sky Blue', 'Cardigan Bomber', 'Crop Cardigan']
stok_list = [2, 4, 6, 8, 10, 12, 13, 15, 16, 18, 20, 21, 24, 35, 38, 40, 45, 60, 70, 75, 90, 95, 100, 120, 125, 200, 210, 250, 255, 260]
harga_list = [20000, 25000, 30000, 33000, 40000, 45000, 50000, 55000, 56000, 60000, 62000, 70000, 71000, 80000, 82000,85000]
pemasok_list = ['Modies', 'Kranggan', 'Perfect', 'Girlsy', 'Clothink', 'Moko Garmen', 'Yenies Shirt', 'Flipper Wear', 'Lumos', 
'Nakano Suit', 'Clothink', 'Moko Garmen', 'Yenies Shirt']

# Frame input untuk menambah item
frame_input = tk.Frame(root, bg='lightblue')
frame_input.pack(pady=20)

tk.Label(frame_input, text="Pilih Barang", font=("Gabriola", 14, "bold"), bg='lightblue').grid(row=0, column=0, padx=5, pady=5, sticky="w")
combo_item = ttk.Combobox(frame_input, values=nama_barang_list)
combo_item.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(frame_input, text="Deskripsi", font=("Gabriola", 14, "bold"), bg='lightblue').grid(row=0, column=2, padx=5, pady=5, sticky="w")
combo_deskripsi = ttk.Combobox(frame_input, values=deskripsi_list)
combo_deskripsi.grid(row=0, column=3, padx=5, pady=5, sticky="w")

tk.Button(frame_input, text="Tambah Item", font=("Courier New", 10, "bold"), bg='black', fg='white', command=tambah_item).grid(row=1, columnspan=2, pady=5)
tk.Button(frame_input, text="Hapus Item", font=("Courier New", 10, "bold"), bg='black', fg='white', command=hapus_item).grid(row=1, column=2, columnspan=2, pady=5)

# Frame output untuk menampilkan inventaris
frame_output = tk.Frame(root)
frame_output.pack(pady=10)

columns = ("Kode Barang", "Nama Barang", "Deskripsi", "Jumlah Stok", "Harga Per Unit", "Status", "Pemasok")
tree_inventaris = ttk.Treeview(frame_output, columns=columns, show="headings", height=10)

for col in columns:
    tree_inventaris.heading(col, text=col, anchor="center")
    tree_inventaris.column(col, width=120, anchor="center")

# Scrollbar untuk Treeview
scrollbar = ttk.Scrollbar(frame_output, orient="vertical", command=tree_inventaris.yview)
tree_inventaris.configure(yscroll=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree_inventaris.pack(fill="both", expand=True)

# Frame untuk menampilkan queue
frame_queue = tk.Frame(root)
frame_queue.pack(pady=10)

columns_queue = ("Kode Barang", "Nama Barang", "Deskripsi")
tree_queue = ttk.Treeview(frame_queue, columns=columns_queue, show="headings", height=5)

for col in columns_queue:
    tree_queue.heading(col, text=col, anchor="center")
    tree_queue.column(col, width=120, anchor="center")

scrollbar_queue = ttk.Scrollbar(frame_queue, orient="vertical", command=tree_queue.yview)
tree_queue.configure(yscroll=scrollbar_queue.set)

scrollbar_queue.pack(side="right", fill="y")
tree_queue.pack(fill="both", expand=True)

# Entry untuk menghapus item
tk.Label(root, text="Kode Barang untuk Dihapus", font=("Gabriola", 12, "bold"), bg='lightblue').pack(pady=10)
entry_delete_code = tk.Entry(root)
entry_delete_code.pack(pady=5)

root.mainloop()