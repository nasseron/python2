class Auto:
    def __init__(self, rekestteritunnus, huippunopeus):
        self.rekestteritunnus = rekestteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0
    def aja(self, tuntia):
        self.matkamittari += min(self.huippunopeus * tuntia, self.rekestteritunnus, self.huippunopeus * 3)
    def __str__(self) -> object:
        return f"Rekisteritunnus: {self.rekestteritunnus}, Huippunopeus: {self.huippunopeus} km/h Matkamittari: {self.matkamittari: .1f} km"
class Sähköauto(Auto):
    def __init__(self, rekestteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekestteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
    def __str__(self):
         return f"{super().__str__()}, Akkukapasiteetti: {self.akkukapasiteetti} KWh"


class polttomoottoriauto(Auto):
    def __init__(self, rekestteritunnus, huippunopeus, bensatankin_kok):
        super().__init__(rekestteritunnus, huippunopeus)
        self.bensatankin_kok = bensatankin_kok
    def __str__(self):
        return f"{super().__str__()}, Bensatankin Kok: {self.bensatankin_kok} 1"
def main(self):
    """  zxzjli

    :rtype: object
    """
    sahkoauto = Sähköauto("ABC-15", 180,52.5)
    polttomoottoriauto = polttomoottoriauto("ACD", 165, 32.3)
    sahkoauto.huippunopeus = 180
    polttomoottoriauto.huippunopeus = 165
    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)
    print(sahkoauto)
    print(polttomoottoriauto)
if __name__=="__main__":
    main()




