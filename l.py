import string

def kata_unik(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        teks = f.read()

    teks = teks.translate(str.maketrans('', '', string.punctuation)).lower()

    kata_unik = set(teks.split())

    kata_urut = sorted(kata_unik)

    for kata in kata_urut:
        print(kata)

nama_file = input("Masukkan nama file: ")
kata_unik(nama_file)

