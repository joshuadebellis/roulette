import random

bankroll = 60
play_again = True
while play_again == True :
    play_again = True

    bet = raw_input("Place your bet: ")
    bankroll = bankroll - int(bet)
    bet_2 = raw_input("red or black? ")
    wheel_spin = random.randint(0,36)
    if wheel_spin % 2 == 0 and bet_2 == "black":
        bankroll = bankroll + 2 * bet
        print "you win!"
        print "your current bankroll is " ,bankroll
        question = raw_input("Would you like to play again? ")
        if question == "yes":
            play_again = True
        else:
            break
        
        
    elif wheel_spin % 2 !=0 and bet_2 == "red":
        bankroll = bankroll + 2 * int(bet)
        print "you win!"
        print "your current bankroll is " ,bankroll
        question = raw_input("Would you like to play again? ")
        if question == "yes":
            play_again = True
        else:
            break
    else:
        bankroll = bankroll - 2 * int(bet)
        print "you lose!"
        print "your current bankroll is " ,bankroll
        question = raw_input("Would you like to play again? ")
        if question == "yes":
            play_again = True
        else:
            break
        
    if bankroll < 0 :
        print "Game Over!"
        break
        
