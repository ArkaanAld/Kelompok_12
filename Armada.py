from abc import ABC, abstractmethod

class Armada(ABC):

    def __init__(self, nama, energi):
        self.nama = nama
        self.__total_km = 0
        self.__energi = energi

    @property
    def total_km(self):
        return self.__total_km

    @total_km.setter
    def total_km(self, km):
        if km > 0:
            self.__total_km += km

    @property
    def energi(self):
        return self.__energi

    @energi.setter
    def energi(self, jumlah):
        if jumlah > 0:
            self.__energi -= jumlah

    @abstractmethod
    def bergerak(self):
        pass

    @abstractmethod
    def berhenti(self):
        pass

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def status(self):
        pass