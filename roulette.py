import random

class Roulette:
    play_again = True
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
        
# initialize variables
play_again = True
bet = 0
bet2 = ''
pot = 0
bankroll = 0

bankroll = int(raw_input("What's your starting pot ? "))
gambling = Roulette(bankroll)

while play_again == True:
    bet = int(raw_input("How much would you like to bet? "))

    valid_bet = False
    while valid_bet != True:
        bet_2 = raw_input("Red or black ? ").lower()
        valid_bet = (bet_2 in ('red', 'black'))
    winner_is_you = gambling.wheelspin(bet, bet_2)
    if winner_is_you:
        print "You win!"
    else:
        print "You lose!"
    print "your current bankroll is " , gambling.bankroll
    question = raw_input("Would you like to play again? ")
    play_again = question == "yes"
    