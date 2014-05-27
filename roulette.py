import random

class Roulette:

    def __init__(self, bankroll):
        self.bankroll = bankroll
    def wheelspin(self, bet, bet_2):
        spin = random.randint(0,36)
        if spin % 2 == 0 and bet_2 == "black" or spin % 2 !=0 and  bet_2 == "red":
            self.bankroll +=  2 * bet
            return True
            
        else:
             self.bankroll -= bet
             return False
             
    def play_game(self):
        self.bet = int(raw_input("How much would you like to bet? "))
        self.bet_2 = raw_input("Red or black ? ").lower()
        winner_is_you = gambling.wheelspin(self.bet, self.bet_2)
        if winner_is_you:
            print "You win!"
            print "your current bankroll is " , gambling.bankroll
        else:
            print "You lose!"
            print "your current bankroll is " , gambling.bankroll
       
        

   

    
play_again = True
bankroll = int(raw_input("What's your starting pot ? "))
gambling = Roulette(bankroll)
while play_again :
    gambling.play_game()
    question = raw_input("Would you like to play again? ")
    if question == "yes":
       play_again = True
    else:
       play_again = False
    
