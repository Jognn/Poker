class Karta:
    kolory = ['♠', '♥', '♣', '♦']
    figury = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']
    def __init__(self, figura, kolor):
        self.kolor = kolor
        self.figura = figura
        self.rodzaj = self.figura + " " + self.kolor