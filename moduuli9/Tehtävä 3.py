class Auto:
    def __init__(self, registeritunnus: object, huipponopeus: object) -> object:

        self.registeritunnus = registeritunnus
        self.huipponopeus = huipponopeus
        self.tamanhetkenen_nupeos = 0
        self.kuljattu_matka = 0

    def kiihdytä(self, nope_muutos):
        uusi_nopeus = self.tamanhetkenen_nupeos + nope_muutos
        if uusi_nopeus < 0:
           self.tamanhetkenen_nupeos = uusi_nopeus
        elif uusi_nopeus > self.huipponopeus:
            self.tamanhetkenen_nupeos = self.huipponopeus
        else:
            self.tamanhetkenen_nupeos = uusi_nopeus
    def kulje(self, tuntimaara):
        self.kuljattu_matka += self.tamanhetkenen_nupeos * tuntimaara


if __name__ == "__main__":
    uusi_auto = Auto("ABC", 142)
    print("Rekisteritunnus : ",uusi_auto.registeritunnus)
    print("Huippunopeus:", uusi_auto.huipponopeus, "km/h")
    print("Tämänhetkeinen nopeus", uusi_auto.tamanhetkenen_nupeos,"km/h")
    print("Kuljettu matka:", uusi_auto.kuljattu_matka, "km/h")
    uusi_auto.kiihdytä(30)
    uusi_auto.kiihdytä(70)
    uusi_auto.kiihdytä(50)
    print(f"Tämänhtkeinen nopeus: {uusi_auto.tamanhetkenen_nupeos} km/h")

    uusi_auto.kiihdytä(-200)
    print(f"Tämänhetkeinen nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkenen_nupeos}")

    uusi_auto.kulje(1.5)
    print(f"Kulettu matkaa kiihdytyksen jälkeen ", uusi_auto.kuljattu_matka, " km/h")