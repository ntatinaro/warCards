from random import shuffle


class Card:
    suits = ("clubs", "diamonds", "hearts", "spades")
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value<c2.value:
            return True
        if self.value == c2.value:
            return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return False
        return False




    def __repr__(self):
        c = self.values[self.value] + " of " + self.suits[self.suit]
        return c

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
        print(self.cards)
        print("Deck")

    def rem_card(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()


class Deal:

    def __init__(self):
        self.deck = Deck()
        self.p1h = []
        self.p2h = []
        for i in range(26):
            x = self.deck.rem_card()
            self.p1h.append(x)

        for j in range(26):
            y = self.deck.rem_card()
            self.p2h.append(y)




class Player:
    def __init__(self, nme, h):
        self.playername = nme
        self.playerhand = h



class Game:

    def __init__(self):
        self.p1n = input("Enter Player 1 Name")
        self.p2n = input("Enter Player 2 Name")
        dl = Deal()
        self.p1hand = getattr(dl, 'p1h')
        self.p2hand = getattr(dl, 'p2h')

        print(self.p1hand)
        print(self.p1n + " Hand")
        print(self.p2hand)
        print(self.p2n + " Hand")




    def wins(self, winner):
        w = "{} Wins this round"
        w = w.format(winner)
        print(w)


    def draw(p1n, p1card, p2n, p2card):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1card, p2n, p2card)
        print(d)

    def play_game(self):
        print("Beginning War!")
        while len(self.p1hand) != 0 and len(self.p2hand) != 0:
            #m = "q to quit" + "any other key to play:"
            #responce = input(m)
            #if responce == "q":
                #break
            x = self.p1hand.pop()
            y = self.p2hand.pop()
            Game.draw(self.p1n, x, self.p2n, y)

            if x > y:
                print(self.p1n + " wins this round")
                self.p1hand.insert(0, x)
                self.p1hand.insert(0, y)
                print(self.p1hand)
            elif x < y:
                print(self.p2n + " wins this round")
                self.p2hand.insert(0, x)
                self.p2hand.insert(0, y)
                print(self.p2hand)
            else:
                print("WARRRRRRRRRRRRRRRRR!")
                x1 = self.p1hand.pop()
                x2 = self.p1hand.pop()
                x3 = self.p1hand.pop()
                x4 = self.p1hand.pop()
                y1 = self.p2hand.pop()
                y2 = self.p2hand.pop()
                y3 = self.p2hand.pop()
                y4 = self.p2hand.pop()
                Game.draw(self.p1n, x4, self.p2n, y4)
                if x4 > y4:
                    print(self.p1n + " wins the war")
                    self.p1hand.insert(0, x)
                    self.p1hand.insert(0, x1)
                    self.p1hand.insert(0, x2)
                    self.p1hand.insert(0, x3)
                    self.p1hand.insert(0, x4)
                    self.p1hand.insert(0, y)
                    self.p1hand.insert(0, y1)
                    self.p1hand.insert(0, y2)
                    self.p1hand.insert(0, y3)
                    self.p1hand.insert(0, y4)
                    print(self.p1hand)
                elif x4 < y4:
                    print(self.p2n + " wins the war")
                    self.p2hand.insert(0, x)
                    self.p2hand.insert(0, x1)
                    self.p2hand.insert(0, x2)
                    self.p2hand.insert(0, x3)
                    self.p2hand.insert(0, x4)
                    self.p2hand.insert(0, y)
                    self.p2hand.insert(0, y1)
                    self.p2hand.insert(0, y2)
                    self.p2hand.insert(0, y3)
                    self.p2hand.insert(0, y4)
                    print(self.p2hand)
                else:
                    print("IDK")
        if len(self.p1hand) == 0:
            print(self.p2n + " Wins the Game")

        if len(self.p2hand) == 0:
            print(self.p1n + " Wins the Game")




gme = Game()
gme.play_game()