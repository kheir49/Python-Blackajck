# Karan Heir
# ID: 501048458
# Code below simply recreates a simplified version of Blackjack
# In the simplified version, the card's are pulled from an infinetely large deck with no faces.
# The only actions the player or computer can take are to hit or stand, and there is also no gambling in this version.


import random

print("Welcome to Blackjack! In this game you will play against the dealer (the computer)")


# Following function deals with computer's Turn
def compTurn(compSum):
    # compSum for the most part will become the new Sum for the computer except in one specific case
    print("\n********************\t\t\tComputer's Turn\t\t********************\n")

    if compSum < 17:
        card = random.randint(1, 11)
        compSum += card
        print("The dealer hit and got:", card)
        print("The dealer's sum is now:", compSum)
    # Computer will always draw a card if they're sum is less than 17
    else:
        print("The dealer stands!")
        compSum = -1
    # This is the one case in which compSum does not become the computer's new sum

    return compSum
    # compSum goes in and out


# Following function deals with player's Turn
def playTurn(playSum):
    # Similarly to compTurn, this playSum will become the player's sum except in one specific case
    print("\n********************\t\t\tYour Turn\t\t\t********************\n")
    valid = False
    # Boolean here is used to delineate the validity of the players actions

    while not valid:
        # If the player's choice is not valid, code will loop

        playChoice = input("What would you like to do this turn?\n> ")
        playChoice = playChoice.lower()
        # I'm not sure whether or not there is a case insensitive comparison,
        # so I simply put all entries into lower case

        if playChoice == "hit" or playChoice == "h":
            card = random.randint(1, 11)
            print("You hit and got:", card)
            playSum += card
            print("Your total sum is now:", playSum)
            valid = True
        elif playChoice == "stand" or playChoice == "s":
            print("You stood!")
            valid = True
            playSum = -1
            # Same as computer turn, playSum here won't become the new Sum
        else:
            print("Please enter a valid command")
            # valid is set to true only if player enters a valid command,
            # otherwise, they repeat the entry of their command.

    return playSum


playWin = 0
dealWin = 0
# Above variables are win Counters

gameOn = True
inPlay = True
# gameOn is used to allow the player to repeat the game as many times as they want
# inPlay is used to determine whether or not the game itself is ongoing
while gameOn:
    dealSum = 0
    playSum = 0

    dealStand = False
    playStand = False

    while inPlay:

        # Computer's turn below
        if not dealStand:
            # Turn will be skipped if dealer stood
            compTurnResult = compTurn(dealSum)
            if compTurnResult > 21:
                print("The dealer went bust!")
                break
                # If the dealer goes bust, there is no point in continuing, so the loop is broken
            elif compTurnResult == -1:
                dealStand = True
                # if the result of the turn is returned as -1,
                # then dealStand will be set to true to skip all subsequent computer turns
            else:
                dealSum = compTurnResult
                # The result returned from compTurn is only made into the dealers sum if they hit and did not go bust
        else:
            print("Computer's turn skipped as computer stood previously stood.")

        # Player's turn below
        if not playStand:
            playTurnResult = playTurn(playSum)
            if playTurnResult > 21:
                print("You went bust!")
                break
                # Similarly to dealer's turn, no point in continuing at this point
            elif playTurnResult == -1:
                playStand = True
                # Same as dealers turn before, playStand set to true if result of playTurn is -1
            else:
                playSum = playTurnResult
                # Only if the player did not go bust will they get a new sum
        else:
            print("You stood previously so your turn has been skipped.")

        if dealStand and playStand:
            print("\nBoth players have stood, and so the game has ended.")
            break
            # If both players stood, there is no need to continue
            # Here I could have simply set inPlay to False, but doing so
            # would require me to set it as True every single loop
            # i.e. inPlay is never set to False at any point, loop is instead broken via code

    print()
    # Instead of placing end="\n" or placing "\n" at every single condition that can exit the inPlay loop,
    # I chose to print a blank line instead
    if playSum > dealSum or dealSum > 21:
        # If player has a higher sum then the dealer OR,
        # If the dealer busts, then the player automatically wins
        print("You won!")
        playWin += 1
    elif dealSum > playSum or playSum > 21:
        # If dealer has a higher sum then the player OR,
        # If the player busts, then the dealer automatically wins
        print("The dealer won!")
        dealWin += 1
    elif dealSum == playSum:
        print("Both players tied; no one won.")

    continueGame = input("\nWould you like to play again? (Enter no or n to stop, all other entries will continue)\n> ")
    continueGame = continueGame.lower()
    if continueGame == "no" or continueGame == "n":
        gameOn = False

print("\n\nYou won", playWin, "times, and the computer won", dealWin, "times.")
print("Thanks for playing!")
