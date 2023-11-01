# Mencetak beberapa teks
print("ABC")
print("X")
print("Y")
print("Z")

# Mengisi nilai dan menetapkkan variabel
w, x, y, z = 10, 15, 20, 25

# Mencetak variabel dengan pemisah yang berbeda
print(w, x, y, z)
print(w, x, y, z, sep="")
print(w, x, y, z, sep=":")
print(w, x, y, z, sep=", ")
print(w, x, y, z, sep="- ")

# Mencetak angka dan hasil pangkatnya
for i in range(11):
    print(i, 10**i)

# Menambah fungsi pemformatan
for i in range(11):
    print("{0:>3} {1:>16}".format(i, 10**i))
