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
        
def play_game():
    bet = int(raw_input("How much would you like to bet? "))
    bet_2 = raw_input("Red or black ? ").lower()
    winner_is_you = gambling.wheelspin(bet, bet_2)
    if winner_is_you:
        print "You win!"
        print "your current bankroll is " , gambling.bankroll
    else:
       print "You lose!"
       print "your current bankroll is " , gambling.bankroll
       
    play_again == raw_input("Would you like to play again? ")
    return play_again

    
play_again = True
bankroll = int(raw_input("What's your starting pot ? "))
gambling = Roulette(bankroll)
if play_again:
    play_game()
    
