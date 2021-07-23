#Side Pot Calculator 
#Take input from user to get value for the main pot 
#Take input from user to get value of lowest bet size player
#Take input from user to get values of all other players remaining in the hand
#Perform calculations to get the amount that needs to be pushed into the main pot 
#Remaining amount will be pushed into side pot
#Inform the user of which individuals can take from the side pot and main pot in the case he/she wins

print('')
print('Welcome to the Side Pot Calculator!')

userChoice = input('CALCULATE SIDE POT? (Y/N): ')
userChoice = userChoice.upper()
print('')

if (userChoice == 'Y'):
    mainPot = int(input('CURRENT VALUE OF POT: '))
    lowestBet = int(input('LOWEST BET AMOUNT: '))
    highestBet = int(input('HIGHEST BET AMOUNT: '))
    playersInHand = int(input('TOTAL PLAYERS IN THE HAND: '))

    mainPotAdd = (lowestBet * playersInHand) + mainPot
    sidePot = ((highestBet - lowestBet) * (playersInHand - 1)) 
    
    print('')
    print('MAIN POT:', mainPotAdd)
    print('SIDE POT:', sidePot)
    print('')

    print('DISTRIBUTION GUIDE')
    print('==================')
    print('IF ALL-IN PLAYER WINS: ')
    print('     ALL-IN PLAYER = MAIN POT')
    print('     RUNNER-UP PLAYER = SIDE POT')
    print('')
    print('IF ALL-IN PLAYER LOSES: ')
    print('     WINNING PLAYER = MAIN POT + SIDE POT')
    print('')
else:
    print('Thank You.')
    print('')







