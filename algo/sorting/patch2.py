# import json
# from prettytable import PrettyTable

# with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
#     dataa = json.load(f)

# data = list(dataa.items())

# def buble_sort():
#     a = 0
#     array = data
#     n = len(array) 
#     for i in range(n):
#         for j in range(n - i - 1): 
#             if array[j][1]["jarak"] > array[j + 1][1]["jarak"]:                
#                 a += 1
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 bukun = [buku[1]['jarak'] for buku in data] 
#                 print(f"step ke {a} : {bukun}, iterasi ke {i + 1}")
#     return array

# buble_sort()

# table = PrettyTable()
# table.field_names = ["nama warung", "jarak"]
# for buku in buble_sort():
#     table.add_row([buku[0], buku[1]['jarak']])
# print(table)

import json
from prettytable import PrettyTable

with open("C:/Users/LENOVO/Downloads/Rumah Makan (Sort)/data.json", "r") as f:
    dataa = json.load(f)

jarak = [buku["jarak"] for buku in dataa.values()]
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

def buble_sort():
    a = 0
    array = data
    n = len(array) 
    for i in range(n):
        for j in range(n - i - 1): 
            if array[j][1]["jarak"] > array[j + 1][1]["jarak"]:                
                a += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                bukun = [buku[1]['jarak'] for buku in data] 
                # print(f"step ke {a} : {bukun}, iterasi ke {i + 1}")
    return array

buble_sort()

print("\nWarung sebelum di sorting")
tabel = list(zip(nama, jarak, status, jam))

table1 = PrettyTable()
table1.field_names = ["nama warung", "rating", "status", "jam tutup"]
for buku in tabel:
    table1.add_row(buku)
print(table1)

print("\nWarung setelah di sorting by rating")

table = PrettyTable()

table = PrettyTable()
table.field_names = ["nama warung", "jarak", "status", "jam tutup"]

for buku in buble_sort():
    jam_buka = datetime.datetime.strptime(buku[1]['jam buka'], "%H:%M").time()
    jam_tutup = datetime.datetime.strptime(buku[1]['jam tutup'], "%H:%M").time()
    if jam_buka <= now <= jam_tutup:
        status = "buka"
    else:
        status = "tutup"
    table.add_row([buku[0], buku[1]['jarak'], status, buku[1]['jam tutup']] )
print(table)
