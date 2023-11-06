import streamlit as st
import datetime

# Panjang teks
panjang = 45

# Login
st.title("Login Casher CwCoffe")
keys = "admin"
login = st.text_input("masukan id: ")
pw = st.text_input("masukan pw: ", type="password")
if st.button("Login"):
    if login == keys and pw == keys:
        st.write("\nAnda berhasil login".center(panjang))
    else:
        st.write("\nPassword salah".center(panjang))

st.write("\nSelamat Datang Di".center(panjang))
st.write("CwCoffe & Eatery".center(panjang))
st.write("\nMENU".center(panjang), "\n")

# Daftar menu dan harganya
minuman = {
    1: {"name": "Robusta Coffe Milk", "price": 17000},
    2: {"name": "Black Sasame Coffe", "price": 23000},
    3: {"name": "Cappicino Cincau", "price": 28000},
    4: {"name": "Arabica Coffe Milk", "price": 20000},
    5: {"name": "Coffe Latte", "price": 22000},
    6: {"name": "Americano Arabica", "price": 14000}
}

makanan = {
    1: {"name": "Beef Bulgogi", "price": 35000},
    2: {"name": "Chicken Steak", "price": 30000},
    3: {"name": "Chicken Katsu", "price": 26000},
    4: {"name": "Nasi Goreng", "price": 35000},
    5: {"name": "Mie Goreng", "price": 35000},
    6: {"name": "Bakso Goreng", "price": 35000}
}

# Cetak daftar menu
st.write("Minuman : ")
for item in minuman.values():
    st.write(f"{item['name']} \t: Rp{item['price']}")

st.write("\nMakanan : ")
for item in makanan.values():
    st.write(f"{item['name']} \t\t: Rp{item['price']}")

# Input nama pelanggan dan nomor meja
nama = st.text_input("nama pelanggan : ")
meja = st.text_input("nomor meja : ")

# Inisialisasi variabel total dan pesanan
total = 0
pesanan = {}

# Pilih menu
while True:
    pilihan = st.text_input("isi menu. 'x' untuk end: ")
    if pilihan.lower() == 'x':
        break
    elif pilihan in [item['name'] for item in makanan.values()] or pilihan in [item['name'] for item in minuman.values()]:
        jenis = ''
        if pilihan in [item['name'] for item in makanan.values()]:
            jenis = 'makanan'
        elif pilihan in [item['name'] for item in minuman.values()]:
            jenis = 'minuman'
        jumlah = st.number_input(f"Masukkan jumlah {pilihan} {jenis} yang dipesan: ")
        if jenis == 'makanan':
            for item in makanan.values():
                if item['name'] == pilihan:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    total += item['price'] * jumlah
                    st.write(f"{pilihan} ditambahkan ke daftar pesanan.")
        elif jenis == 'minuman':
            for item in minuman.values():
                if item['name'] == pilihan:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    total += item['price'] * jumlah
                    st.write(f"{pilihan} ditambahkan ke daftar pesanan.")
    else:
        st.write("Menu tidak valid. Silakan pilih menu yang tersedia.")

# Cetak pesanan dan total
for item, jumlah in pesanan.items():
    st.write(f"{item} \t: {jumlah}")
st.write(f"total Rp {total}")

# Hitung pajak dan total harga
pajak = total * 0.11
total_pajak = pajak + total

# Pilih metode pembayaran
metode = st.radio("metode pembayaran", ("cash", "e-money"))
if metode == "e-money":
    e = total_pajak
    eme = "e-money"
    sungsong = 0
else:
    bayar = st.number_input("bayaran : ")
    em = "cash"
    sungsong = bayar - total
    bayar1 = bayar
    while True:
        if bayar < total:
            st.write("uang tidak cukup")
            bayar = st.number_input("bayaran : ")
        else:
            break

st.write("\n\n")

# Informasi toko
tokoh = "CWCoffe & Eatery"
jln = "Dansen"
alamat = "Jl Danau Sentarum No. 30, Sungai Bangkok, Kec."
kota = "Pontianak Kota"
no_hp = "08517441286"
tanggal_waktu_sekarang = datetime.datetime.now()
tanggal_waktu_diformat = tanggal_waktu_sekarang.strftime("%Y/%m/%d %H:%M:%S")
casir = "Dansen Cw Coffe"

# Cetak struk
st.write(tokoh.center(panjang))
st.write(jln.center(panjang))
st.write(alamat.center(panjang))
st.write(kota.center(panjang))
st.write(no_hp.center(panjang))
st.write(f"Nomor meja : {meja}".center(panjang))
st.write("")
st.write("="*panjang)
st.write( '%-24s %20s' % ("Order Date", tanggal_waktu_diformat))
st.write( '%-24s %20s' % ("Cashier", casir))
st.write("="*panjang)
st.write("")
st.write("Nama pemesan : ", nama)
for item, jumlah in pesanan.items():
    st.write(f"{item} \t: {jumlah}")
st.write("="*panjang)
st.write( '%-24s %20s' % ("Subtotal", total))
st.write( '%-24s %20s' % ("pajak", pajak))
st.write( '%-24s %20s' % ("Total", total_pajak))
st.write("")
if metode == "cash":
    st.write( '%-24s %20s' % (em, bayar1))
elif metode == "e-money":
    st.write( '%-24s %20s' % (eme, e))
st.write( '%-24s %20s' % ("Kembali", sungsong))
st.write("")
st.write("CWCoffe.id".center(panjang))
st.write("\n")
st.write("Thanks for stopping by.".center(panjang))
