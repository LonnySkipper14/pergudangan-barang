from prettytable import PrettyTable

class Barang:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

class Penjualan:
    def __init__(self, nama_barang, jumlah, total, uang_dibayar, kembalian, sisa_pembayaran):
        self.nama_barang = nama_barang
        self.jumlah = jumlah
        self.total = total
        self.uang_dibayar = uang_dibayar
        self.kembalian = kembalian
        self.sisa_pembayaran = sisa_pembayaran

class Pergudangan:
    def __init__(self):
        self.list_barang = []
        self.transaksi = []
        self.penjualan = []

    def tambah_barang(self, nama_barang, jumlah, harga):
        for barang in self.list_barang:
            if barang.nama == nama_barang:
                barang.jumlah += jumlah
                break
        else:
            new_barang = Barang(nama_barang, jumlah, harga)
            self.list_barang.append(new_barang)

        self.transaksi.append(f"Tambah {jumlah} {nama_barang} dengan harga {harga} per item.")
        print(f"{jumlah} {nama_barang} berhasil ditambahkan ke stok. Stok sekarang: {self.list_barang[-1].jumlah}.")

    def keluarkan_barang(self, nama_barang, jumlah):
        for barang in self.list_barang:
            if barang.nama == nama_barang and barang.jumlah >= jumlah:
                barang.jumlah -= jumlah
                total_penjualan = barang.harga * jumlah
                uang_dibayar, kembalian, sisa_pembayaran = self.input_uang_dibayar(total_penjualan)
                self.penjualan.append(Penjualan(nama_barang, jumlah, total_penjualan, uang_dibayar, kembalian, sisa_pembayaran))
                self.transaksi.append(f"Terjual {jumlah} {nama_barang}.")
                print(f"{jumlah} {nama_barang} berhasil dikeluarkan dari stok. Stok sekarang: {barang.jumlah}.")
                return True
        print("Stok tidak mencukupi atau barang tidak ditemukan.")
        return False
    def input_uang_dibayar(self, total):
        uang_dibayar = 0

        print(f"Masukkan jumlah uang dibayar (Total: {total}): ")
        while True:
            try:
                nominal = float(input("Masukkan nominal: "))
                if nominal >= total:
                    uang_dibayar += nominal
                    kembalian = uang_dibayar - total
                    sisa_pembayaran = 0
                    print(f"Kembalian: {kembalian}")
                    break
                else:
                    sisa_pembayaran = total - nominal
                    kembalian = 0
                    print(f"Jumlah uang dibayar kurang dari total. Sisa pembayaran: {sisa_pembayaran}.")
            except ValueError:
                print("Masukkan angka yang valid untuk nominal.")

        return uang_dibayar, kembalian, sisa_pembayaran

    def tampilkan_tabel_barang(self):
        if not self.list_barang:
            print("Stok kosong.")
        else:
            table = PrettyTable()
            table.field_names = ["Nama Barang", "Jumlah", "Harga", "Total"]
            table.align["Nama Barang"] = "l"
            table.align["Jumlah"] = "r"
            table.align["Harga"] = "r"
            table.align["Total"] = "r"
            table.horizontal_char = '-'
            table.vertical_char = '|'
            table.junction_char = '+'

            for barang in self.list_barang:
                total = barang.jumlah * barang.harga
                table.add_row([barang.nama, barang.jumlah, barang.harga, total])

            print("Tabel Stok Barang:")
            print(table)

    def tampilkan_rincian_transaksi(self):
        if not self.transaksi:
            print("Belum ada transaksi.")
        else:
            print("Rincian Transaksi:")
            for i, transaksi in enumerate(self.transaksi, 1):
                print(f"{i}. {transaksi}")

    def tampilkan_rincian_penjualan(self):
        if not self.penjualan:
            print("Belum ada penjualan.")
        else:
            print("Rincian Penjualan:")
            table = PrettyTable()
            table.field_names = ["Nama Barang", "Jumlah", "Total", "Uang Dibayar", "Kembalian"]
            table.align["Nama Barang"] = "l"
            table.align["Jumlah"] = "r"
            table.align["Total"] = "r"
            table.align["Uang Dibayar"] = "r"
            table.align["Kembalian"] = "r"
            table.horizontal_char = '-'
            table.vertical_char = '|'
            table.junction_char = '+'

            for item in self.penjualan:
                table.add_row([item.nama_barang, item.jumlah, item.total, item.uang_dibayar, item.kembalian])

            print(table)

def main():
    pergudangan = Pergudangan()

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Transaksi Barang")
        print("3. Tampilkan Rincian Transaksi")
        print("4. Tampilkan Rincian Stok Barang")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang yang ditambahkan: "))
            harga = float(input("Masukkan harga barang: "))
            pergudangan.tambah_barang(nama_barang, jumlah, harga)

        elif pilihan == "2":
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang yang dikeluarkan: "))
            pergudangan.keluarkan_barang(nama_barang, jumlah)
            pergudangan.tampilkan_rincian_penjualan()

        elif pilihan == "3":
            pergudangan.tampilkan_rincian_transaksi()

        elif pilihan == "4":
            pergudangan.tampilkan_tabel_barang()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
