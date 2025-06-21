import json
from sharedpublic import queue_dict
from QueueManagement import simpan_queue
from queue_loader import load_data_ke_queue  
import os

load_data_ke_queue("rekening", "rekening.json")
load_data_ke_queue("cc", "cc.json")
load_data_ke_queue("masalah", "masalah.json")

def layani_antrian(jenis, file_json): #serve the queue
    q = queue_dict[jenis]
    if q.is_empty():
        print(f"Tidak ada antrian untuk {jenis}.")
    else:
        pelanggan = q.serve()
        if pelanggan:
            kode = q.format_nomor(pelanggan['nomor'])
            print(f"Melayani: {pelanggan['nama']} ({kode})")
            simpan_queue(file_json, q.queue)
            simpan_last_served(jenis, pelanggan)

def simpan_last_served(jenis, data): #save the queue that is being served
    with open("last_served.json", "r+") as file:
        try:
            semua = json.load(file)
        except:
            semua = {}
        semua[jenis] = data
        file.seek(0)
        json.dump(semua, file, indent=4) 
        file.truncate()

if not os.path.exists("last_served.json"): 
    with open("last_served.json", "w") as f:
        json.dump({}, f)

def main():
    while True:
        print("\n=== Panel Customer Service ===")
        print("1. Layani Antrian Rekening")
        print("2. Layani Antrian Credit Card")
        print("3. Layani Antrian Masalah")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            layani_antrian("rekening", "rekening.json")
        elif pilihan == "2":
            layani_antrian("cc", "cc.json")
        elif pilihan == "3":
            layani_antrian("masalah", "masalah.json")
        elif pilihan == "4":
            print("Keluar dari panel CS.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
