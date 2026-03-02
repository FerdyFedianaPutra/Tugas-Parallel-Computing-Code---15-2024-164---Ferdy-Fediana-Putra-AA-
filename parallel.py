import multiprocessing
import os

def hitung_kuadrat(angka):
    print(f"Proses ID: {os.getpid()} menghitung {angka}^2")
    return angka * angka

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    # Membuat pool sejumlah core CPU
    with multiprocessing.Pool() as pool:
        hasil = pool.map(hitung_kuadrat, data)

    print("\nHasil akhir:", hasil)
