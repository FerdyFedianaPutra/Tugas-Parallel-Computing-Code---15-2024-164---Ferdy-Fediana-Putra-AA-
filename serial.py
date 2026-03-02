total = 0

print("Menghitung jumlah angka dari 1 sampai 10...\n")

for i in range(1, 11):
    print(f"Menambahkan {i}")
    total = total + i

rata_rata = total / 10

print("\nHasil akhir:")
print("Total =", total)
print("Rata-rata =", rata_rata)
