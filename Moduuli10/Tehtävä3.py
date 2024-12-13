import  random

class Hissi:
    def __init__(self, aliman_kerros, ylimmän_kerros):

        self.aliman_kerros = aliman_kerros
        self.ylimmän_kerros = ylimmän_kerros
        self.nykyinen_kerros = aliman_kerros
        print(f"Hissi on alimassa kerroksessa:", self.nykyinen_kerros)

    def kerros_ylös(self):
        self.nykyinen_kerros < self.ylimmän_kerros
        self.nykyinen_kerros += 1

    def kerros_alas(self):
        self.nykyinen_kerros > self.aliman_kerros
        self.nykyinen_kerros -= 1

    def siirry_kerroksen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        print("Hissi siirty kerroksen: ", self.nykyinen_kerros)

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()
        print("Hissi siirty kerrksen:", self.nykyinen_kerros)


class Talo:
    def __init__(self, alimmainen_kerros, ylimmainen_kerros, hissien_lukumäärä):
        self.alimmainen_kerros = alimmainen_kerros
        self.ylimmainen_kerros = ylimmainen_kerros
        self.hissit = [Hissi(alimmainen_kerros, ylimmainen_kerros) for i in range(hissien_lukumäärä)]
        print(
            f"Talo luotu: {hissien_lukumäärä} hissiä, alimat ja ylmmät kerrokset: {alimmainen_kerros, ylimmainen_kerros}")

    def aja_hissijä(self, hissi_numero, kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Siirrytään hissiin {hissi_numero + 1} ja mennään kerrokseen {kerros}")
            self.hissit[hissi_numero].siirry_kerrokseen(kerros)
        else:
            print("ValueError")


def palohälytys(self):
    print("Palohölytys! kaikki hissit menevät  pohjakerrokseen .....")
    for hissi in self.hissit:
        hissi.siirry_kerroksen(self.alimmainen_kerros)
def main():
    Talo = Talo(1, 10, 3)
    talo.aja_hissiä(0, 5)
    talo.aja_hissiä(2, 8)
    talo.aja_hissiä(1, 3)
    talo.palohälytys()

print("Kaikki hissiä ovat pohjassakerroksessa.)")
if __name__ == "__main__":
    main()