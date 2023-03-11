import datetime
import time

# Tanggal Ramadan 2023
ramadan_date = datetime.datetime(2023, 3, 23)

while True:
    # Waktu saat ini
    current_date = datetime.datetime.now()

    # Selisih waktu antara waktu saat ini dengan tanggal Ramadan 2023
    time_left = ramadan_date - current_date

    # Konversi selisih waktu ke dalam format Hari:Jam:Menit:Detik
    days, seconds = time_left.days, time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    # Hapus tulisan sebelumnya dari layar
    print("\033[F\033[K", end="")

    # Tampilkan waktu yang tersisa dengan warna biru
    print(f"\033[94mHitungan Mundur menuju Ramadhan 2023: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds\033[0m", end="\r")

    # Jeda selama 1 detik sebelum iterasi berikutnya
    time.sleep(1)
