from data import Tes

def print_buku_by_kategori():
    ts_instance = Tes()
    kategori_list = ["Fiksi", "Non-Fiksi", "Sains", "Komedi"]

    for kategori in kategori_list:
        hasil_filter = ts_instance.filter_buku_by_kategori(kategori)

        if hasil_filter:
            print(f"\nBuku dengan kategori '{kategori}':")
            for judul, buku_info in hasil_filter.items():
                print(f"Judul: {judul}, Tersedia: {buku_info['tersedia']}")
        else:
            print(f"Tidak ada buku dengan kategori '{kategori}'.")

# Contoh pemanggilan fungsi print_buku_by_kategori
print_buku_by_kategori()