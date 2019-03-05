"""
We are impplimenting BlackJack game using python.
This game will have 1 human player and a computer dealer.
"""
import random
class Blackjack():
    cardsindeck = 52
    mini_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = mini_deck*4

    def __init__(self):
        print ("BlackJack Game")

    def play_blackjack(self):
        playgame = input("Play BlackJack ? Press Y/N \n")
        
        while playgame.upper() == 'Y':
            print ("Starting BlackJack Game!")
            playername = input("Player Name : ")
            playerbalance = int(input("Player Balance : "))
            print ("Staring Game ! Get Ready {}".format(playername))
            print ("Shuffling deck!")
            random.shuffle(self.deck)
            player_cards = []
            computer_cards = []
            player_cards.append(Blackjack.hit(self))
            player_cards.append(Blackjack.hit(self))
            print ("Player Cards : \n")
            print (player_cards)
            computer_cards.append(Blackjack.hit(self))
            computer_cards.append(Blackjack.hit(self))
            print ("computer Cards : \n")
            print (computer_cards[0])
            player_cards_totalvalue = sum(player_cards)
            computer_cards_totalvalue = sum(computer_cards)
            whoWon=''

            if (player_cards_totalvalue == 21 and computer_cards_totalvalue!=21):
                print ("Jackpot!! {} WON!! 1 PlayerTotalValue : {} ComputerTotalValue : {}".format(playername, player_cards_totalvalue, computer_cards_totalvalue))
                whoWon = 'Player'
                break
            
            elif (player_cards_totalvalue == 21 and computer_cards_totalvalue == 21):
                print ("No One WINS!! 2".format(playername))
                playgame = input("Play BlackJack Again ? Press Y/N \n")
                break

            while (player_cards_totalvalue <21):
                playerChoice = input("Want to hit deck or stay ? Choose H/S \n")

                if (playerChoice.upper() == 'H'):
                    print ("hitting deck1")
                    player_cards.append(Blackjack.hit(self))
                    player_cards_totalvalue = sum(player_cards)
                    print (player_cards_totalvalue)
                    if (player_cards_totalvalue == 21):
                        print ("{}  WON!! 3 PlayerTotalValue : {} ComputerTotalValue : {}".format(playername, player_cards_totalvalue, computer_cards_totalvalue))
                        break
                    elif (player_cards_totalvalue > 21):
                        print ("Computer Won!! 4 PlayerTotalValue : {} ComputerTotalValue : {}".format(player_cards_totalvalue, computer_cards_totalvalue))
                        break
                        
                else:
                    while (computer_cards_totalvalue <17):
                        print ("hitting deck2")
                        computer_cards.append(Blackjack.hit(self))
                        computer_cards_totalvalue = sum(computer_cards)
                        print (computer_cards_totalvalue)
                        if (computer_cards_totalvalue == 21):
                            print ("Computer Wims!! 5 PlayerTotalValue : {} ComputerTotalValue : {}".format(player_cards_totalvalue,computer_cards_totalvalue))
                            break
                        elif (computer_cards_totalvalue > 21):
                            print ("{} WINS!!! 6 PlayerTotalValue : {} ComputerTotalValue : {}".format(playername,player_cards_totalvalue,computer_cards_totalvalue))
                            break
                    if (computer_cards_totalvalue == 21):
                        print ("Computer Wims!! 7 PlayerTotalValue : {} ComputerTotalValue : {}".format(player_cards_totalvalue,computer_cards_totalvalue))
                        break
                    elif (computer_cards_totalvalue > 16 and computer_cards_totalvalue < 21):
                        if (computer_cards_totalvalue > player_cards_totalvalue):
                            print ("Computer Won!! 8 PlayerTotalValue : {} ComputerTotalValue : {}".format(player_cards_totalvalue,computer_cards_totalvalue))
                            break
                        elif (computer_cards_totalvalue < player_cards_totalvalue):
                            print ("{}  WON!! 9 PlayerTotalValue : {} ComputerTotalValue : {}".format(playername,player_cards_totalvalue,computer_cards_totalvalue))
                            break
                        else:
                            print ("Play Ends!!!")
                            break
                    playgame = input("Play BlackJack ? Press Y/N \n")
                    break
                            
                        

                
    def hit(self):
        rand_pick = random.randint(1,len(self.deck))
        card = self.deck.pop(rand_pick)
        print (card)
        return card

    def stand(self):
        pass
            
            







my_blackjack = Blackjack()
my_blackjack.play_blackjack()
