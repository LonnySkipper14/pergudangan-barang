from tabulate import tabulate

nama = []
cari_pesanan = []

# List Daftar Menu
menuMakanan = [
    ["1", "Steak Ayam", "Rp. 25.000"],
    ["2", "Steak Sirlon Sapi", "Rp. 45.000"],
    ["3", "Steak Kambing", "Rp. 45.000"],
    ["4", "Nasi Gurih", "Rp. 15.000"],
    ["5", "Nasi Goreng", "Rp. 25.000"],
    ["6", "Mie Ayam", "Rp. 15.000"],
    ["7", "Dimsum Ayam", "Rp. 15.000"],
    ["8", "Dimsum Sapi", "Rp. 20.000"],
    ["9", "Dimsum Jamur", "Rp. 15.000"],
    ["10", "Keripik Ubi", "Rp. 5.000"],
]
hargaMakanan = [25000, 45000, 45000, 15000,
                25000, 15000, 15000, 20000, 15000, 5000]

menuMinuman = [
    ["1", "Jus Apel", "Rp. 15.000"],
    ["2", "Jus Jeruk", "Rp. 15.000"],
    ["3", "Jus Alpukat", "Rp. 15.000"],
    ["4", "Jus Mangga", "Rp. 15.000"],
    ["5", "Cappucino", "Rp. 15.000"],
    ["6", "Air Mineral", "Rp. 10.000"],
    ["7", "Kopi Tubruk", "Rp. 10.000"]
]
hargaMinuman = [15000, 15000, 15000, 15000, 15000, 10000, 10000]

menuTambahan = [
    ["A", "Nasi Uduk", "Rp. 5.000"],
    ["B", "Nasi Putih", "Rp. 5.000"],
    ["C", "Kuah Soto", "Rp. 5.000"],
]
hargaTambahan = [5000, 5000, 5000, 0]

print("================================================")
print("Daftar Menu Cafe ABC")
print("================================================")
print("\n Menu Makanan")
print(tabulate(menuMakanan, tablefmt="grid", headers=[
    "No.", "Menu Makanan", "Tarif"], numalign="center", stralign="center"))
print("\n Menu Minuman")
print(tabulate(menuMinuman, tablefmt="grid", headers=[
    "No.", "Menu Minuman", "Tarif"], numalign="center", stralign="center"))
print("\n Menu Tambahan")
print(tabulate(menuTambahan, tablefmt="grid", headers=[
    "Pilihan", "Menu Tambahan", "Tarif"], numalign="center", stralign="center"))
print("\t")


def pesanan():

    # Percabangan Menu Makanan
    nama_pelanggan = input("Masukkan Nama Pelanggan: ")
    kode_makanan = input("Masukkan Kode Makanan: ")
    if kode_makanan == "1":
        Makanan = (menuMakanan[0][1])
        tarif_makanan = (hargaMakanan[0])
    elif kode_makanan == "2":
        Makanan = (menuMakanan[1][1])
        tarif_makanan = (hargaMakanan[1])
    elif kode_makanan == "3":
        Makanan = (menuMakanan[2][1])
        tarif_makanan = (hargaMakanan[2])
    elif kode_makanan == "4":
        Makanan = (menuMakanan[3][1])
        tarif_makanan = (hargaMakanan[3])
    elif kode_makanan == "5":
        Makanan = (menuMakanan[4][1])
        tarif_makanan = (hargaMakanan[4])
    elif kode_makanan == "6":
        Makanan = (menuMakanan[5][1])
        tarif_makanan = (hargaMakanan[5])
    elif kode_makanan == "7":
        Makanan = (menuMakanan[6][1])
        tarif_makanan = (hargaMakanan[6])
    elif kode_makanan == "8":
        Makanan = (menuMakanan[7][1])
        tarif_makanan = (hargaMakanan[7])
    elif kode_makanan == "9":
        Makanan = (menuMakanan[8][1])
        tarif_makanan = (hargaMakanan[8])
    elif kode_makanan == "10":
        Makanan = (menuMakanan[9][1])
        tarif_makanan = (hargaMakanan[9])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")