def create_diamond(rows):
    # Penerapan jarak sebelum bintang
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print("* " * (i + 1))

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)


# Masukan jumlah pola berlian
rows = int(input("Masukkan jumlah baris pola: "))
create_diamond(rows)
