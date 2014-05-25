import random


    
    
class Roulette(object):
    play_again = True
    def __init__(self,bet,bet_2, bankroll):
        self.bet = bet 
        self.bet_2 = bet_2
        self.bankroll = bankroll
    def wheelspin(self):
        spin = random.randint(0,36)
        if spin % 2 == 0 and bet_2 == "black":
            self.bankroll +=  2 * int(self.bet)
            print "you win!"
            print "your current bankroll is " , self.bankroll
            question = raw_input("Would you like to play again? ")
            if  question == "yes":
                play_again = True
            else:
                play_again = False
        
        elif spin % 2 !=0 and  bet_2 == "red":
            self.bankroll = int(self.bankroll) + 2 * int(self.bet)
            print "you win!"
            print "your current bankroll is " ,self.bankroll
            question = raw_input("Would you like to play again? ")
            if  question == "yes":
                 play_again = True
            else:
                 play_again = False
        else:
             self.bankroll = int(self.bankroll) - 2 * int(self.bet)
             print "you lose!"
             print "your current bankroll is " , self.bankroll
             question = raw_input("Would you like to play again? ")
             if  question == "yes":
                 play_again = True
             if  question == "no" :
                 play_again = False
             

                 
        return 0
        
        

bankroll = raw_input("What's your starting pot ? ")
bet = int(raw_input("Place your Bet! "))
bet_2 = raw_input("Red or Black ? ")
Gambling = Roulette(bet, bet_2, bankroll)
while Gambling.play_again == True:
    Gambling = Roulette(bet, bet_2, bankroll)
    Gambling.wheelspin()
        
        
    