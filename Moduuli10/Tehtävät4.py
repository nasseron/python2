import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljet_matka = 0

    def Kiihdyytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.kuljet_matka += self.nopeus * tuntimäärä

    def __str__(self):
        return f"{self.rekisteritunnus:<15} {self.huippunopeus:<15} {self.nopeus:<15} {self.kuljet_matka:<15}"

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.uniform(-10, 15)  # Corrected this line
            auto.Kiihdyytä(nopeuden_muutos)  # Corrected the method call
            auto.kulje(1)  # Assuming the time that passes is 1 hour

    def tulosta_tilanne(self):
        print(f"\nKilpailun tilanne: {self.nimi}")
        print(f"{'Rekisteritunnus':<15} {'Huippunopeus':<15} {'Nopeus':<15} {'Kuljet Matka'}")
        for auto in self.autot:
            print(auto)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljet_matka >= self.pituus:
                return True
        return False

def main():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)  # Corrected this line

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    tunti = 0
    while not kilpailu.kilpailu_ohi():
        tunti += 1
        kilpailu.tunti_kuluu()
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()
    kilpailu.tulosta_tilanne()

if __name__ == '__main__':
    main()