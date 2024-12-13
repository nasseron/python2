class Hissi:
    def __init__(self,aliman_kerros, ylimmän_kerros ):

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
        print("Hissi siirty kerroksen: ",self.nykyinen_kerros)

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()
        print("Hissi siirty kerrksen:", self.nykyinen_kerros)



if __name__ == '__main__':
    hissi = Hissi(-2, 10)
    hissi.siirry_kerroksen(5)
    hissi.siirry_kerroksen(-3)



