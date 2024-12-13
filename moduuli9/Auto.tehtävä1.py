class Auto:
    def __init__(self, registeritunnus, huipponopeus):
        self.registeritunnus = registeritunnus
        self.huipponopeus = huipponopeus
        self.tamanhetkenen_nupeos = 0
        self.kuljattu_matka = 0

if __name__== '__main__':
        uusi_auto = Auto("Abc-123 " ,142)
        print(f"Rekisteritunnus: {uusi_auto.registeritunnus}")
        print(f"Huippunopeus: {uusi_auto.huipponopeus} km/h")
        print(f"Tämänhetkeinen nopeues: {uusi_auto.tamanhetkenen_nupeos} km/h")
        print(f"Kuljettu matka: {uusi_auto.kuljattu_matka} km")




