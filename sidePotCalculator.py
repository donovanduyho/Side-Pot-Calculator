#Side Pot Calculator 
print('')
print('Welcome to the Side Pot Calculator!')

userChoice = input('CALCULATE SIDE POT? (Y/N): ')
userChoice = userChoice.upper()
print('')

if (userChoice == 'Y'): 
    #Convert input into int type
    currentPot = int(input('CURRENT VALUE OF POT: '))

    #Intialize list 
    playerBetList = []
    #Takes total players and stores into variable
    #Convert input into int type
    n = int(input('REMAINING PLAYERS IN HAND: '))
    print('')

    #For loop used to append into user inputs list 
    #Parameter begins at 1 in order to make sense for user
    for i in range(1, n+1):
        print('ENTER BET AMOUNT FOR PLAYER', i)
        #Stores input into variable, convert to int, and append into list
        player = int(input())
        playerBetList.append(player)

    print('ALL PLAYER BETS: ', playerBetList)
    print('')

    #Takes minimum value in list and store into variable
    lowestPlayerBet = min(playerBetList)
    highestPlayerBet = max(playerBetList)

    #Main Pot Formula: (lowest bet * players in hand) + current pot 
    #Side Pot Formula: (highest bet - lowest bet) * (players in hand - 1)
    mainPot = (lowestPlayerBet * n) + currentPot
    sidePot = (highestPlayerBet - lowestPlayerBet) * (n - 1)

    #Print players that are allowed to take the main pot
    #Everyone can take the main pot
    print('MAIN POT:', mainPot)
    print('------------------------')
    for i,bet in enumerate(playerBetList,1):
        print('PLAYER', i, '|', 'BET SIZE: ', bet)

    print('')

    #Print players that are allowed to take the side pot
    #Everyone except the lowest better can take the side pot
    print('SIDE POT:', sidePot)
    print('------------------------')
    for i,bet in enumerate(playerBetList,1):
        if(bet == highestPlayerBet):
            print('PLAYER', i, '|', 'BET SIZE: ', bet)

    print('')
    print('QUICK REMINDER: ')
    print('- LOWEST BETTER IS ONLY ALLOWED TO TAKE THE MAIN POT')
    print('- ANYONE OTHER THAN THE LOWEST BETTER IS ALLOWED TO TAKE BOTH POTS')
    print('')
    print('THANK YOU')
    print('')
else:
    print('THANK YOU')
    print('')