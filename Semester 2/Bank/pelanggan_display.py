from sharedpublic import queue_dict
from QueueManagement import simpan_queue
from queue_loader import load_data_ke_queue

load_data_ke_queue("rekening", "rekening.json")
load_data_ke_queue("cc", "cc.json")
load_data_ke_queue("masalah", "masalah.json")

def tambah_antrian(jenis, nama, file_json):
    q = queue_dict[jenis]
    q.tambah_queue(nama)
    simpan_queue(file_json, q.queue)

def main():
    while True:
        print("\n=== Sistem Pengambilan Antrian ===")
        print("1. Ambil Antrian")
        print("2. Keluar")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            print('''Jenis Antrian: 
    1. Pembuatan Rekening 
    2. Credit Card 
    3. Penanganan Masalah''')

            jenis = input("Masukkan jenis antrian (1-3): ")
            nama = input("Masukkan nama Anda: ")

            if jenis == '1':
                tambah_antrian("rekening", nama, "rekening.json")
            elif jenis == '2':
                tambah_antrian("cc", nama, "cc.json")
            elif jenis == '3':
                tambah_antrian("masalah", nama, "masalah.json")
            else:
                print("Jenis antrian tidak valid.")
        elif pilihan == "2":
            print("Terima kasih telah menggunakan sistem antrian!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
