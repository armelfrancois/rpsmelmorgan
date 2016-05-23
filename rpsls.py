import random
rpsls = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def lizardSpock(rpsls):
    lives =  5
    while lives != 0:
        playerChoice = input('Make your choice: ')
        computerChoice = random.choice(rpsls)
        #rock
        if playerChoice == 'rock':
            if computerChoice == 'rock':
                print('The computer chose: ', computerChoice)
                print('Draw')
                continue
            elif computerChoice == 'paper':
                print('The computer chose: ', computerChoice)
                print('Loose')
                lives = lives - 1
                continue
            elif computerChoice == 'scissors':
                print('The computer chose: ', computerChoice)
                print('Win')
                continue
            elif computerChoice == 'lizard':
                print('The computer chose: ', computerChoice)
                print('Win')
                continue
            elif computerChoice == 'spock':
                print('The computer chose: ', computerChoice)
                print('Loose')
                lives = lives - 1
                continue
            else:
                print('Make a valid choice!')
                continue
        #paper
        if playerChoice == 'paper':
            if computerChoice == 'rock':
                print('The computer chose: ', computerChoice)
                print('Win')
                continue
            elif computerChoice == 'paper':
                print('The computer chose: ', computerChoice)
                print('Draw')
                lives = lives - 1
                continue
            elif computerChoice == 'scissors':
                print('The computer chose: ', computerChoice)
                print('Loose')
                continue
            elif computerChoice == 'lizard':
                print('The computer chose: ', computerChoice)
                print('Loose')
                continue
            elif computerChoice == 'spock':
                print('The computer chose: ', computerChoice)
                print('Win')
                lives = lives - 1
                continue
            else:
                print('Make a valid choice!')
                continue
    
lizardSpock(rpsls)
    
    
