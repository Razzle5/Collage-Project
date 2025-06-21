import json

class queue:
    def __init__(self, prefix):
        self.queue = []
        self.nomor_terakhir = 0
        self.prefix = prefix
        self.terakhir_dilayani = None

    def queue_code(self):#queue format next queue
        return f"{self.prefix}{self.nomor_terakhir:03d}"
    
    def format_nomor(self, nomor):#input format queue
        return f"{self.prefix}{nomor:03d}"
    
    def tambah_queue(self, nama):
        self.nomor_terakhir += 1
        kode = self.queue_code()
        data = {"nomor": self.nomor_terakhir, "nama": nama}
        self.queue.append(data)
        print(f"{nama} masukkan queue dengan nomor {kode}")

    def serve(self):
        if not self.queue:
            return None
        data = self.queue.pop(0)
        self.terakhir_dilayani = data 
        return data
    
    def peek(self):
        return self.queue[0] if self.queue else None

    def peek_next(self):
        return self.queue[1] if len(self.queue) > 1 else None

    def is_empty(self):
        return len(self.queue) == 0

    def tampilan_queue(self):
        if not self.queue:
            print("Antrian Kosong")
        else:
            print("\nDaftar antrian saat ini:")
            for data in self.queue:
                kode = self.format_nomor(data["nomor"])
                print(f"Nomor {kode} : {data['nama']}")

def simpan_queue(nama_file, data_queue):
    with open(nama_file, "w") as file:
        json.dump(data_queue, file, indent=4)

def queue_load(nama_file):
    try:
        with open(nama_file, "r") as file:
            isi = file.read().strip()
            if not isi:
                return []
            return json.loads(isi)
    except FileNotFoundError:
        return []
