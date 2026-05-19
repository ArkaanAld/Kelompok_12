from Armada import Armada

class AngkotModern(Armada):

    def __init__(self, nama, energi, setoran):
        super().__init__(nama, energi)

        self.setoran = setoran

    def bergerak(self):

        print(f"{self.nama} sedang bergerak")

        km = float(input("Masukkan jarak tempuh: "))

        self.total_km = km
        self.energi = km

    def berhenti(self):

        print(f"{self.nama} sedang berhenti")

    def hitung_biaya(self):

        return (self.total_km * 1000) - self.setoran

    def status(self):

        print("\n=== STATUS ANGKOT MODERN ===")
        print("Nama:", self.nama)
        print("Total KM:", self.total_km)
        print("Energi:", self.energi)
        print("Setoran:", self.setoran)
        print("Biaya:", self.hitung_biaya())