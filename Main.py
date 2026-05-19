from Bus import BusListrik
from Angkot import AngkotModern

daftar_armada = []

while True:

    print("\n===== SISTEM ARMADA =====")
    print("1. Tambah Bus")
    print("2. Tambah Angkot")
    print("3. Jalankan Armada")
    print("4. Lihat Status")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":

        nama = input("Nama Bus: ")
        energi = float(input("Energi: "))
        kapasitas = int(input("Kapasitas: "))

        bus = BusListrik(nama, energi, kapasitas)

        daftar_armada.append(bus)

    elif pilih == "2":

        nama = input("Nama Angkot: ")
        energi = float(input("Energi: "))
        setoran = int(input("Setoran: "))

        angkot = AngkotModern(nama, energi, setoran)

        daftar_armada.append(angkot)

    elif pilih == "3":

        if len(daftar_armada) == 0:
            print("Belum ada armada")
            continue

        for i, armada in enumerate(daftar_armada):

            print(f"{i}. {armada.nama}")

        index = int(input("Pilih armada: "))

        daftar_armada[index].bergerak()
        daftar_armada[index].berhenti()

    elif pilih == "4":

        if len(daftar_armada) == 0:
            print("Belum ada armada")
            continue

        for armada in daftar_armada:

            armada.status()

    elif pilih == "5":

        print("Program selesai 🚍")
        break

    else:

        print("Menu tidak valid")