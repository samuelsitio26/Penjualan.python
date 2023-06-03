# Inisialisasi variabel
nama_toko = "Toko Buku Python"
total_harga = 0
daftar_beli = []

# Input daftar belanja
while True:
    buku = input("Masukkan nama buku (ketik 'selesai' untuk mengakhiri): ")
    if buku.lower() == "selesai":
        break
    harga = float(input("Masukkan harga buku: "))
    jumlah_beli = int(input("Masukkan jumlah buku yang dibeli: "))
    
    subtotal = harga * jumlah_beli
    total_harga += subtotal
    
    daftar_beli.append({"Buku": buku, "Harga": harga, "Jumlah": jumlah_beli, "Subtotal": subtotal})

# Cetak struk pembelian
print("===============================")
print(f"Struk Pembelian Buku - {nama_toko}")
print("===============================")
for beli in daftar_beli:
    print(f"Nama Buku: {beli['Buku']}")
    print(f"Harga Satuan: Rp. {beli['Harga']}")
    print(f"Jumlah Beli: {beli['Jumlah']}")
    print(f"Subtotal: Rp. {beli['Subtotal']}")
    print("===============================")
print(f"Total Harga: Rp. {total_harga}")
print("===============================")
print(f"Terima kasih telah berbelanja di {nama_toko}!")
