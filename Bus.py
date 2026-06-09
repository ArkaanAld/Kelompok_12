from Armada import Armada

class BusListrik(Armada):

    def __init__(self, nama, energi, kapasitas):
        super().__init__(nama, energi)
        self.kapasitas = kapasitas

    def bergerak(self):
        print(f"{self.nama} sedang bergerak")
        km = float(input("Masukkan jarak tempuh: "))
        self.total_km = km
        self.energi = km * 2

    def berhenti(self):
        print(f"{self.nama} sedang berhenti")
    def hitung_biaya(self):
        return self.total_km * 1500

    def status(self):
        print("\n=== STATUS BUS LISTRIK ===")
        print("Nama:", self.nama)
        print("Total KM:", self.total_km)
        print("Energi:", self.energi)
        print("Kapasitas:", self.kapasitas)
        print("Biaya:", self.hitung_biaya())
