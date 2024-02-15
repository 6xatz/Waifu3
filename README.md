## Mata Kuliah

Sebagai tugas praktikum: [3] Bahasa Pemrograman | Universitas Pelita Bangsa.

## Laporan Praktikum

- Latihan 1:

  > Mencetak teks menggunakan Python dengan beberapa ketentuan.

  <p align="left">
    <img src="/ss/1.jpg" width="500">
  </p>

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

perintah dan fungsi sudah dijelaskan pada bagian **_#_**.

- Latihan 2:

  > Latihan 2 sudah terdapat pada **_Praktikum 2 (Waifu2)_** -> **_Latihan 3_** dan sudah pernah dikerjakan.

- Latihan 3:

  > bisa saja menggunakan **_string format_** tapi kurang efisien.

  <p align="left">
    <img src="/ss/2.jpg" width="500">
  </p>

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

- Menghitung keliling dan luas lingkaran beserta Flowchart-nya:
  <p align="left">
    <img src="/ss/3.jpg" width="400">
    <img src="/ss/flowchart.jpg" width="400">
  </p>

      # Masukan jumlah jari-jari lingkaran
      jari_jari = float(input("Masukkan jari-jari lingkaran: "))

      # Menghitung luas dan keliling dengan konstanta
      luas = 3.14 * jari_jari**2
      keliling = 2 * 3.14 * jari_jari

      # Mencetak hasil penjumlahan
      print(f"Luas lingkaran: {luas}\nKeliling lingkaran: {keliling}")

## Documentation

All associated resources. are licensed under the [MIT License](https://mit-license.org/).
