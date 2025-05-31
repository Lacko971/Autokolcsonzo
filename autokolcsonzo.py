from abc import ABC, abstractmethod
from datetime import datetime

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ulesek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    def __str__(self):
        return f"Személyautó: {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, {self.ulesek_szama} ülés"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó: {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, {self.teherbiras} kg"
class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.rendszam} ({self.auto.tipus}) - {self.datum.strftime('%Y-%m-%d')}"
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadasa(self, auto):
        self.autok.append(auto)

    def auto_berlese(self, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Nincs ilyen rendszámú autó."
        if any(b.auto.rendszam == rendszam and b.datum == datum for b in self.berlesek):
            return "Az autó már foglalt ezen a napon."
        self.berlesek.append(Berles(auto, datum))
        return f"Bérlés sikeres, ár: {auto.berleti_dij} Ft"

    def berles_lemondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                return "Bérlés lemondva."
        return "Nincs ilyen bérlés."

    def berlesek_listazasa(self):
        return [str(b) for b in self.berlesek]
kolcsonzo = Autokolcsonzo("CityRent")
kolcsonzo.auto_hozzaadasa(Szemelyauto("ABC123", "Opel Astra", 10000, 5))
kolcsonzo.auto_hozzaadasa(Szemelyauto("XYZ987", "Suzuki Swift", 8000, 4))
kolcsonzo.auto_hozzaadasa(Teherauto("TRK555", "Ford Transit", 15000, 1200))
kolcsonzo.auto_berlese("ABC123", datetime(2025, 6, 2))
kolcsonzo.auto_berlese("XYZ987", datetime(2025, 6, 3))
kolcsonzo.auto_berlese("TRK555", datetime(2025, 6, 4))
kolcsonzo.auto_berlese("XYZ987", datetime(2025, 6, 5))
def menu():
    while True:
        print("\n1. Autó bérlése\n2. Bérlés lemondása\n3. Bérlések listázása\n4. Kilépés")
        valasz = input("Választás: ")
        if valasz == "1":
            rendszam = input("Rendszám: ")
            datum_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                print(kolcsonzo.auto_berlese(rendszam, datum))
            except ValueError:
                print("Hibás dátumformátum.")
        elif valasz == "2":
            rendszam = input("Rendszám: ")
            datum_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                print(kolcsonzo.berles_lemondasa(rendszam, datum))
            except ValueError:
                print("Hibás dátumformátum.")
        elif valasz == "3":
            for b in kolcsonzo.berlesek_listazasa():
                print(b)
        elif valasz == "4":
            break
        else:
            print("Érvénytelen választás.")
if __name__ == "__main__":
    menu()
