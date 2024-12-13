import random

class Auto:
    def __init__(self, registeritunnus):
        self.registeritunnus = registeritunnus
        self.huipponopeus = random.randint(100, 200)
        self.nopeus = 0  # Initialize speed
        self.kuljettu_matka = 0  # Fixed variable name

    def kiihdytä(self):
        muutos = random.randint(-10, 15)
        self.nopeus = min(self.huipponopeus, max(0, self.nopeus + muutos))

    def kulje(self):
        self.kuljettu_matka += self.nopeus

def main():
    autot = [Auto(f"ABC-{i+1}") for i in range(10)]  # Create a list of Auto objects

    for tunti in range(1, 11):
        print(f"Tunti {tunti}")
        for auto in autot:
            auto.kiihdytä()
            auto.kulje()
            print(f"{auto.registeritunnus}: Nopeus: {auto.nopeus} km/h, Kuljettu matka: {auto.kuljettu_matka} km")

if __name__ == "__main__":
    main()