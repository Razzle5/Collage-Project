from sharedpublic import queue_dict
from QueueManagement import queue_load
#This file is used to load recent the JSON file.

def load_data_ke_queue(jenis, nama_file):
    try:
        data = queue_load(nama_file)
        q = queue_dict[jenis]
        q.queue = data

        if data:
            # take the last data [ ] and nomor [ ]
            last_nomor = data[-1]["nomor"]

            # only take the last number not string like R,C,or M
            if isinstance(last_nomor, str) and last_nomor[0].isalpha():
                last_nomor = int(last_nomor[1:])
            
            q.nomor_terakhir = int(last_nomor)
            print(f"Antrian '{jenis}' dimuat. Nomor terakhir: {q.nomor_terakhir}")
        else:
            q.nomor_terakhir = 0
            print(f"Antrian '{jenis}' masih kosong. Mulai dari awal.")
    except Exception as e:
        print(f"Gagal memuat antrian '{jenis}' dari '{nama_file}': {e}")