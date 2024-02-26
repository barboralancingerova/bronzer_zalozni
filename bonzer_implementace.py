from bonzer_kontrakt import AbstractKontejner, AbstractNotifikator, AbstractObserver, Karta

class Observer(AbstractObserver):   #načte id karty, vymysli zpravu rodicum
    def __init__(self, databaze: AbstractKontejner, notifikator: AbstractNotifikator) -> None:
        self.databaze = databaze
        self.notifikator = notifikator

    def vstup(self, id:int) -> bool:
        karta = self.databaze.ctecka(id)
        telo_zpravy = "Žák "+karta.jmeno+" právě dorazil do školy."
        self.notifikator.zprava(karta.mail, telo_zpravy)
        return True

class Kontejner(AbstractKontejner):   #z id karty zjistí ostatní údaje
    def __init__(self) -> None:
        self.data : dict[int,Karta]= {}
        self.data[1] = Karta(1, "Karel Pilny", 123456789, "karel@pilny.arcig.cz")
        self.data[2] = Karta(2, "Adam Vesely", 125678789, "adam@vesely.arcig.cz")
        self.data[3] = Karta(3, "Anezka Mala", 123456789, "anezka@mala.arcig.cz")
        self.data[4] = Karta(4, "Daniel Novak", 1256328269, "daniel@novak.arcig.cz")
        self.data[5] = Karta(5, "Linda Stastna", 1238568356, "linda@stastna.arcig.cz")

    def ctecka(self, id: int) -> Karta:
        return self.data[id]

class Notifikator(AbstractNotifikator):   #napise zpravu rodicum, odesila zpravu rodicum
    def zprava(self, mail: str, telo_zpravy: str) -> None: 
        print("Na mail: "+mail+ " posílám oznámení: "+ telo_zpravy)
    ...

def build() -> AbstractObserver:
    databaze = Kontejner()
    notifikator = Notifikator()
    observer = Observer(databaze, notifikator)
    return observer

app = build()
app.vstup(5)