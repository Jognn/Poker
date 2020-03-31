from random import randint

class Player:
    def __init__(self, name, saldo):
        self.name = name
        self.saldo = saldo
        self.karty = list()
        self.zaklad = 0
        self.rozdanie = None
        self.passuje = False
        self.all_in = False

    def dobierz(self):
        i = randint(0, len(self.rozdanie.talia)-1)
        self.karty.append(self.rozdanie.talia[i])
        self.rozdanie.talia.pop(i)

    def wyswietl_karty(self):
        try:
            print(f"Reka gracza {self.name}:  {self.karty[0].rodzaj} || {self.karty[1].rodzaj}")
        except IndexError:
            raise IndexError(f"Gracz nie dobral wszystkich kart!")

    def bet(self, ilosc):
        if self.saldo + self.zaklad - ilosc < 0:
            return False
        self.rozdanie.najwiekszy_zaklad = ilosc
        self.saldo += self.zaklad - ilosc
        self.zaklad = ilosc
        self.rozdanie.pula += ilosc
        print(f"\t - {self.name} obstawia {ilosc}")
        return True

    def info(self):
        if not self.rozdanie.wylozone == []:
            print("Wylozone: " + " || ".join(x.rodzaj for x in self.rozdanie.wylozone))
            self.wyswietl_karty()
        print(f"Obecny zaklad: {self.zaklad} \t Minimalna stawka: {self.rozdanie.najwiekszy_zaklad} \t Saldo: {self.saldo}")

    def wybor(self):
        print("-----------------------------------------------------------------")
        bet = "ALL-IN" if self.rozdanie.najwiekszy_zaklad >= self.zaklad + self.saldo else "BET"
        akcja_flag = False

        while not akcja_flag:
            self.info()
            akcja = input(f"   PASS || ALL || BET *kwota* \t or \t P || A || B *kwota*\n \t").upper()
            if akcja == "PASS" or akcja == "P":
                self.passuje = True
                akcja_flag = True
            elif akcja[0] == "B" or akcja[0:3] == "BET": ### ERROR GDY SIE NIE PODA LICZBY, INPUT TYPU 9-1 DAJE LICZBE 91 ###
                wartosc = int("".join([str(x) for x in akcja if x.isdigit()])) # Zamienia na ladna liczbe
                if self.rozdanie.najwiekszy_zaklad > wartosc:
                    print(f"Minimalna stawka wynosi {self.rozdanie.najwiekszy_zaklad}!")
                else:
                    if self.bet(wartosc):
                        akcja_flag = True
                    else:
                        print(f"Nie dysponujesz takim budzetem!")
            elif akcja == "ALL" or akcja == "A" or akcja == "ALL-IN":
                self.bet(self.saldo)
                self.all_in = True
                akcja_flag = True
            else:
                print("Prosze podac odpowiednia akcje!")

    def koniec_tury(self):
        self.zaklad = 0
