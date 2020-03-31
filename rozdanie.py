from random import randint

class Rozdanie:
    def __init__(self, talia, gracze):
        self.running = True
        self.talia = talia
        self.gracze = gracze
        self.kolej = self.gracze[0]
        self.kolej_nr = self.gracze.index(self.kolej)
        self.rozpoczynajacy = self.gracze[(self.kolej_nr+2)%len(self.gracze)]

        self.nr_tury = 1
        self.wylozone = list()
        self.pula = 0
        self.maly_blind = 5
        self.najwiekszy_zaklad = 0

    def karty_info(self):
        print("-------------------------------------------------------------------------")
        for gracz in self.gracze:
            print(f"Gracz {gracz.name}:")
            for karta in gracz.karty:
                print("\t - " + karta.rodzaj)

        print(f"\n NA STOLE: ({len(self.wylozone)})")
        for karta in self.wylozone:
            print("\t - " + karta.rodzaj)

        print(f"\n POZOSTALE: ({len(self.talia)})")
        for karta in self.talia:
            print("\t - " + karta.rodzaj)
        print("-------------------------------------------------------------------------")

    def przegral(self):
        self.gracze.pop(self.kolej_nr)
        print(f"\t - Gracz {self.kolej.name} passuje")

    def nastepny(self):
        if self.kolej.passuje: # Osoba zpassowala
            self.przegral()
            self.kolej_nr = self.kolej_nr % len(self.gracze)
        else:
            self.kolej_nr = (self.kolej_nr+1) % len(self.gracze)

        self.kolej = self.gracze[self.kolej_nr]
        print(f"\n\nKolej gracza: {self.kolej.name}")

        if len(self.gracze) == 1:
            print(f"\t - Gracz {self.kolej.name} wygrywa")
            self.running = False

    def rozpocznij(self):
        for n in range(len(self.gracze)): # Przekaz graczom referencje
            self.gracze[n].rozdanie = self
        i = 1
        print(f"Kolej gracza: {self.kolej.name}")
        while not self.pula == 3*self.maly_blind:
            if self.kolej.bet(i*self.maly_blind):
                i += 1
            else:
                self.kolej.passuje = True
            self.nastepny()

    def sprawdz_bety(self):
        return all(gracz.zaklad == self.najwiekszy_zaklad for gracz in self.gracze)

    def tura(self, poczatek=False):
        if not poczatek:
            self.kolej = self.rozpoczynajacy
        print(f"***TURA NR {self.nr_tury}***")
        print(f"Kolej gracza: {self.kolej.name}")

        while True: ### TO DO: UPIEKSZYC ####
            self.kolej.wybor()
            if self.sprawdz_bety():
                break
            self.nastepny()
        print(f"***Koniec tury {self.nr_tury}***\n\n")

        self.nr_tury += 1
        self.najwiekszy_zaklad = 0
        for gracz in self.gracze:
            gracz.koniec_tury()

    def rozdaj_karty(self):
        for x in range(2):
            for gracz in self.gracze:
                gracz.dobierz()

    def wyloz_karty(self, ilosc):
        for x in range(ilosc):
            i = randint(0, len(self.talia)-1)
            self.wylozone.append(self.talia[i])
            self.talia.pop(i)

    def run(self):
        self.rozpocznij()
        self.tura(True)

        self.rozdaj_karty()
        self.wyloz_karty(3)

        for i in range(2):
            self.wyloz_karty(1)
            self.tura()

        self.karty_info()








