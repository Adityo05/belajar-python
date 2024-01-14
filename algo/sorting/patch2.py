import json
from prettytable import PrettyTable
import time
import datetime

def buble_sort():
    global array
    global now
    with open("C:/Users/LENOVO/Downloads/Rumah Makan (Sort)/data.json", "r") as f:
        dataa = json.load(f)

    data = list(dataa.items())
    now = datetime.datetime.now().time()
  
    a = 0
    waktuM = time.time()
    array = data
    n = len(array) 
    for i in range(n):
        for j in range(n - i - 1): 
            if array[j][1]["jarak"] > array[j + 1][1]["jarak"]:                
                a += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                bukun = [buku[1]['jarak'] for buku in data] 
                print(f"step ke {a} : {bukun}, iterasi ke {i + 1}")

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def stat():
    global hasil
    global array
    buble_sort()
    result_list = []
    for warung in array:
        jam_buka = datetime.datetime.strptime(warung[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(warung[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        jrk = warung[1]['jarak']
        if jrk > 1000:
            jarak = f"{jrk / 1000} KM"
        else:
            jarak = f"{jrk} M"

        result_list.append({
            "Nama warung": warung[0],
            "jarak": jarak,
            "status": status,
            "jam buka": warung[1]['jam buka'],
            "jam tutup": warung[1]['jam tutup']
        })

    hasil = result_list

def buble_sort2():
    stat()
    global array
    global now

    now = datetime.datetime.now().time()
    array = list(hasil)

    a = 0
    waktuM = time.time()
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j]["status"] > key_item["status"]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
        print(f"step ke-{a + 1} : {[warung['status'] for warung in array]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def stat2():
    buble_sort2()
    table = PrettyTable()
    table.field_names = ["Nama warung", "jarak", "status", "jam buka", "jam tutup"]
    for warung in array:
        table.add_row([warung["Nama warung"], warung['jarak'], warung['status'], warung['jam buka'], warung['jam tutup']])
    print(table)


