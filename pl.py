def tiga_bilangan_terbaik(lst):
    return sorted(set(lst), reverse=True)[:3]
bilangan = [10, 20, 30, 20, 10, 40, 50, 30]
hasil = tiga_bilangan_terbaik(bilangan)
print("Tiga bilangan terbaik:", hasil)