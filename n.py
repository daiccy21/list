def hitung_rata_rata():
    angka = []
    while True:
        s = input("Masukkan bilangan (ketik 'done' selesai): ")
        if s == "done":
            if angka:
                print("Rata-rata:", sum(angka)/len(angka))
            else:
                print("Tidak ada bilangan.")
            break
        try:
            angka.append(float(s))
        except:
            print("Input salah")
hitung_rata_rata()