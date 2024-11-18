import csv
import random
from faker import Faker

# Inisialisasi Faker
fake = Faker("id_ID")

# Jumlah data yang ingin dibuat
jumlah_data = 1000

# Nama file CSV
filename = 'data_faker.csv'

# Menulis data ke file CSV
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["nama_depan", "nama_belakang", "tanggal", "bulan", "tahun"])
    
    # Menulis header
    writer.writeheader()
    
    # Menulis baris data
    for _ in range(jumlah_data):
        # Menghasilkan data palsu
        nama_depan = fake.first_name().lower()
        nama_belakang = fake.last_name().lower()
        tanggal = fake.day_of_month()
        bulan = fake.month()

        # Menghasilkan tahun acak di bawah 2005
        tahun = random.randint(1980, 2004)

        # Menulis baris ke CSV
        writer.writerow({
            "nama_depan": nama_depan,
            "nama_belakang": nama_belakang,
            "tanggal": tanggal,
            "bulan": bulan,
            "tahun": tahun
        })

print(f'File {filename} telah berhasil dibuat dengan {jumlah_data} entri.')
