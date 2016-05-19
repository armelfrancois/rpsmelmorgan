'''
This is my version of your code
I haven't changed too much of the logic or the ideas
However:
    I'm using a lot more functions, I think this makes it more readable
    I think using global is better than a billion parameters
    And, I've changed the main game a bit, using more if statements instead of while loops
If anyone sees a problem, or has any ideas, say something

Obviously this isn't a fully completed code, so only the PlayGame and Quit functions have been coded
'''


import random
import time
import sys
lives = 3
score = 0
rpsArray = ['rock', 'paper', 'scissors']

def menu():
    print('1) Play Game')
    print('2) Instructions (not done)')
    print('3) Highscore (not done)')
    print('4) Settings (not done)')
    print('5) Quit')
    choice = int(input(''))
    if choice == 1:
        game()
    elif choice == 2:
        instructions()
    elif choice == 3:
        highscore()
    elif choice == 4:
        settings()
    elif choice == 5:
        quitMenu()
    else:
        print('Sorry, I did not understand that..')
        print('')
        time.sleep(1)
        menu()

def game():
    global lives
    global score
    global name
    streak = 0
    gameOver = False
    while lives > 0:
            if streak == 2:
                lives = lives + 1
                streak = 0
            print('')
            pChoice = input('Rock, Paper, Scissors: ')
            cChoice = random.choice(rpsArray)
            print('The computer chose ' + cChoice + '!')
            if pChoice.upper() == 'ROCK':
                if cChoice == 'rock':
                    print('You drew!')
                    score = score + 1
                    streak = 0
                elif cChoice == 'scissors':
                    print('YOU WON!')
                    score = score + 3
                    streak = streak + 1
                elif cChoice == 'paper':
                    print('You lost')
                    lives = lives-1
                    streak = 0
            elif pChoice.upper() == 'SCISSORS':
                if cChoice == 'rock':
                    print('You lost')
                    score = score + 1
                    streak = 0
                elif cChoice == 'scissors':
                    print('You drew!')
                    score = score + 3
                    streak = 0
                elif cChoice == 'paper':
                    print('YOU WON!')
                    lives = lives-1
                    streak = streak + 1
            elif pChoice.upper() == 'PAPER':
                if cChoice == 'rock':
                    print('YOU WON!')
                    score = score + 1
                    streak = streak + 1
                elif cChoice == 'scissors':
                    print('You lost')
                    streak = 0
                    score = score + 3
                elif cChoice == 'paper':
                    print('You drew!')
                    streak = 0
                    lives = lives-1
            else:
                print('fault')
                
    f=open("Highscore.txt","a+")
    f.close()
    f=open("Highscore.txt","r+")
    
    data=f.read().split('\n')
    if not ((len(data)-1)==0):
        for i in range(0,len(data)-1):
            data[i]=data[i].split(',')
            data[i][1]=int(data[i][1])
    data[len(data)-1]=[name,score]
    for i in range(0, len( data)-1 ):
        for k in range( len( data ) -1, i, -1 ):
          if ( data[k][1] < data[k - 1][1] ):
            tmp=data[k]
            data[k]=data[k-1]
            data[k-1]=tmp
    i=0
    while(len(data)>i and i <10):
        f.write(data[i][0])
        f.write(',')
        f.write(str(data[i][1]))
        f.write('\n')
        i+=1
    f.close
        
        
            

#def instructions():

def highscore():
    f=open("Highscore.txt","a+")
    f.close()
    f=open("Highscore.txt","r")
    data=f.read().split('\n')
    if 0==len(data)-1:
        print('No HightScores')
    else:
        for i in range(0,len(data)-1):
            data[i]=data[i].split(',')
            print('Name: '+str(data[i][0]))
            print('Score: '+str(data[i][1]))
            print("____________________________________________")
            if(i==9):
                break
            

#def instructions():

#def highscore():

#def settings():
    

def quitMenu():
    print('Are you sure you want to quit?')
    choice = input('Yes/No: ')
    if choice == 'yes':
        sys.exit()
    if choice == 'no':
        time.sleep(0.5)
        print('')
        menu()

def main():
    global name
    print('Welcome to Rock, Paper, Scissors!')
    name = input('Please enter your name: ')
    print('Hello ' + name + '!')
    print('')
    time.sleep(0.5)
    menu()


main()
