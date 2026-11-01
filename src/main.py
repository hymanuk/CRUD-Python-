import os
import lib.file as fl
import pandas as pd

menu = f'''
===================================================================
    
        Selamat datang di Aplikasi Catatan Penjualan Harian

===================================================================
Silahkan pilih menu yang tersedia:
    1. Tambah Data Penjualan
    2. Lihat Data Penjualan
    3. Edit Data Penjualan
    4. Hapus Data Penjualan
    5. Keluar dari Program

'''

table = {
    'Nama': [],
    'Harga': [],
    'Volume': [],
    'Total': []

}

try:
    df = pd.read_csv('./data/data.csv')
except FileNotFoundError:
    if not os.path.isdir('./data'):
        os.makedirs('./data')
    df = pd.DataFrame(table)
    df.to_csv('./data/data.csv', index=False, encoding='utf-8')
    



while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)

    choose_menu = int(input("Pilih menu yang akan di jalankan : "))

    match choose_menu:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            name = input("Masukkan Nama Barang\t: ")
            price = int(input("Masukkan Harga Barang\t: "))
            volume = int(input("Masukkan Volume Barang\t: "))

            fl.create(name, price, volume, file_name='./data/data.csv')

            print("Barang Telah Ditambahkan di Data. Tekan Tombol Enter Jika Ingin Melanjutkan. *-->")

        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')

            fl.read('./data/data.csv')

            print("\nData Telah Ditampilkan. Tekan Tombol Enter Jika Ingin Melanjutkan. *-->")
            input()

        case 3:
            os.system('cls' if os.name == 'nt' else 'clear')

            fl.read('./data/data.csv')

            name = input("Pilih Barang yang akan Diupdate\t:")

            name_update = input("Masukkan Nama Barang\t: ")
            price_update = int(input("Masukkan Harga Barang\t: "))
            volume_update = int(input("Masukkan Volume Barang\t: "))
            
            fl.update(name_update, price_update, volume_update, file_name='./data/data.csv', name_update=name)            
            
            print("Data Telah Diperbaruri. Tekan Tombol Enter Jika Ingin Melanjutkan. *-->")
            input()

        case 4:
            os.system('cls' if os.name == 'nt' else 'clear')

            fl.read('./data/data.csv')

            name = input("Pilih Nama Barang yang akan di Hapus\t: ")

            fl.delete(file_name='./data/data.csv', name_delete=name)

            print("Barang Telah Dihapus di Data. Tekan Tombol Enter Jika Ingin Melanjutkan. *-->")
            input()
        case 5:
            break



                    


    
