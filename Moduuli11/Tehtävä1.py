class Julkaisia:
    def __init__(self, name):
        self.name = name

    def __tulost_tiedot__(self):
        print("Julkaisjan nimi ", self.name)

class Kirja(Julkaisia):
    def __init__(self, name,  Kirjoittaja, sivumäärä):
        super().__init__(name)
        self.Kirjoittaja = Kirjoittaja
        self.sivumäärä = sivumäärä

    def __tulost_tiedot__(self):
        print("kirjan nimi on ", self.name)
        print("Kirjoittaja nimi on ", self.Kirjoittaja)
        print("Kirjassa on ", self.sivumäärä, "sivumäärä")

class Lehti(Julkaisia):
    def __init__(self,name,  Päätoimittaja ):
        super().__init__(name)
        self.Päätoimittaja = Päätoimittaja

    def __tulost_tiedot__(self):
        print("Lehti nimi on ", self.name)
        print("Päätoimittajan nimi on" ,self.Päätoimittaja)


lehti = Lehti(name="AKU Ankh", Päätoimittaja="Aki Hyyppä")
kirja = Kirja(name="Hytti n:0 6," ,Kirjoittaja="Rose Lissome", sivumäärä=200)
print(lehti.__tulost_tiedot__())
print(kirja.__tulost_tiedot__())

