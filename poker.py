from karta import Karta
from player import Player
from rozdanie import Rozdanie

class Poker:
    def __init__(self):
        self.running = True
        self.talia = [Karta(figura, kolor) for kolor in Karta.kolory for figura in Karta.figury]
        self.jogn = Player("Jogn", 1000)
        self.gracze = [Player("Bot1", 1000), Player("Bot2", 1000), Player("Bot3", 1000), Player("Bot4", 1000)]

    def main(self):
        rozdanie = Rozdanie(self.talia, self.gracze)
        rozdanie.run()

    def wyswietl_talie(self):
        print("_______________________________________________________________________________")
        print(f"\t Talia:  {len(self.talia)}")
        for karta in self.talia:
            print(karta.rodzaj)
        print("_______________________________________________________________________________")

if __name__ == "__main__":
    gra = Poker()
    gra.main()
    #gra.wyswietl_talie()






