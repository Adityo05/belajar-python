import json
from prettytable import PrettyTable

with open("C:/Users/LENOVO/Downloads/Rumah Makan (Sort)/data.json", "r") as f:
    dataa = json.load(f)

rekomendasi = [buku["rekomendasi"] for buku in dataa.values()]
nama = [buku for buku in dataa.keys()]
status = []
jam = []

import datetime
now = datetime.datetime.now().time()



for restaurant, info in dataa.items():
    jam_buka = datetime.datetime.strptime(info["jam buka"], "%H:%M").replace(tzinfo=datetime.timezone.utc).time()
    jam_tutup = datetime.datetime.strptime(info["jam tutup"], "%H:%M").replace(tzinfo=datetime.timezone.utc).time()
    if jam_buka <= now <= jam_tutup:
        status.append("buka")
    else:
        status.append("tutup")
    jam.append(info["jam tutup"])

data = list(dataa.items())

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if data[j][1]["rekomendasi"] > data[max_idx][1]["rekomendasi"]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
    return data

sorted_data = selection_sort(data)

print("\nWarung sebelum di sorting")
tabel = list(zip(nama, rekomendasi, status, jam))
table1 = PrettyTable()
table1.field_names = ["Nama Warung", "Rekomendasi", "Status", "Jam Tutup"]
for buku in tabel:
    table1.add_row(buku)
print(table1)

table = PrettyTable()
table.field_names = ["Nama Warung", "Rekomendasi", "Status", "Jam Tutup"]
for buku in sorted_data:
    jam_buka = datetime.datetime.strptime(buku[1]['jam buka'], "%H:%M").time()
    jam_tutup = datetime.datetime.strptime(buku[1]['jam tutup'], "%H:%M").time()
    if jam_buka <= now <= jam_tutup:
        status = "buka"
    else:
        status = "tutup"
    table.add_row([buku[0], buku[1]['rekomendasi'], status, buku[1]['jam tutup']] )

print(table)
