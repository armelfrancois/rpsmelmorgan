# Rock Paper Scissors

from tkinter import *
import random
import time
import sys

#event is useless, the code doesn't work without it though so...
event = 0

window = Tk()
window.geometry('550x700')
window.wm_title('Rock Paper Scissors')
rpsArray = ['Rock', 'Paper', 'Scissors']

lives = 3
score = 0
streak = 0
highscore = 0

canvasOne = Canvas(window, width = 550, height = 700)
canvasOne.pack()

def rpsStart(event):
    canvasOne.delete(ALL)
    welcome = canvasOne.create_text(275,250, text = 'Play', font = ('Avenir Next', 40))
    highscore = canvasOne.create_text(275, 450, text = 'Highscores', font = ('Avenir Next', 25))
    settings = canvasOne.create_text(275, 550, text = 'Settings', font = ('Avenir Next', 25))
    canvasOne.bind('<Button-1>', menuChoice)
    canvasOne.pack()

def showHighscores():
    global highscore
    canvasOne.delete(ALL)
    showScore = canvasOne.create_text(275,250, text = 'You have stood:', font = ('Avenir Next', 25))
    showScoreTwo = canvasOne.create_text(275,300, text = highscore, font = ('Avenir Next', 30))
    showScoreThree = canvasOne.create_text(275,350, text = 'rounds against the computer', font = ('Avenir Next', 25))
    canvasOne.unbind('<Button-1>')
    canvasOne.pack()
    window.update()
    canvasOne.bind('<Button-1>', rpsStart)
    canvasOne.pack()

def settings():
    canvasOne.delete(ALL)
    hard = canvasOne.create_text(275,250, text = 'Hard', font = ('Avenir Next', 25))
    medium = canvasOne.create_text(275,350, text = 'Medium', font = ('Avenir Next', 25))
    easy = canvasOne.create_text(275,450, text = 'Easy', font = ('Avenir Next', 25))
    canvasOne.unbind('<Button-1>')
    canvasOne.pack()
    window.update()
    canvasOne.bind('<Button-1>', settingsChoice)
    canvasOne.pack()

def settingsChoice(event):
    global lives
    if event.y < 300:
        lives = 1
        print(lives)
    elif event.y > 400:
        lives = 3
        print(lives)
    else:
        lives = 2
        print(lives)
    rpsStart(event)

def menuChoice(event):
    if 400 < event.y < 500:
        #not coded
        showHighscores()
    elif 500 < event.y < 600:
        #not coded
        settings()
    else:
        rpsScreen(event)

def rpsScreen(event):
    global rps
    global lives
    global score
    global highscore
    canvasOne.unbind('<Button-1>')
    window.update()
    canvasOne.delete(ALL)
    homeRect = canvasOne.create_rectangle(475,25,525,75, fill = 'Orange')
    firstRect = canvasOne.create_rectangle(225,450,325,550, fill = 'Blue')
    secondRect = canvasOne.create_rectangle(75,450,175,550, fill = 'Red')
    thirdRect = canvasOne.create_rectangle(375,450,475,550, fill = 'Green')
    rock = canvasOne.create_text(125, 500, text = 'Rock', font = ('Avenir Next', 20))
    paper = canvasOne.create_text(275, 500, text = 'Paper', font = ('Avenir Next', 20))
    scissors = canvasOne.create_text(425, 500, text = 'Scissors', font = ('Avenir Next', 20))
    rps = canvasOne.create_text(275, 250, text = 'Rock Paper Or Scissors?', justify = CENTER, font = ('Avenir Next', 30))
    canvasOne.bind('<Button-1>', playerInput)
    canvasOne.pack
    if lives == 0:
        canvasOne.delete(ALL)
        youLost = canvasOne.create_text(275, 250, text = 'YOU LOST', font = ('Avenir Next',30))
        lives = 3
        if highscore < score:
            highscore = score
        score = 0
        canvasOne.unbind('<Button-1>')
        canvasOne.pack()
        window.update()
        canvasOne.bind('<Button-1>', rpsStart)
        canvasOne.pack()
    elif lives == 1:
        firstHeart = canvasOne.create_oval(25,25,75,75, fill = 'red')
    elif lives == 2:
        firstHeart = canvasOne.create_oval(25,25,75,75, fill = 'red')
        secondHeart = canvasOne.create_oval(100,25,150,75, fill = 'red')
    elif lives == 3:
        firstHeart = canvasOne.create_oval(25,25,75,75, fill = 'red')
        secondHeart = canvasOne.create_oval(100,25,150,75, fill = 'red')
        thirdHeart = canvasOne.create_oval(175,25,225,75, fill = 'red')
        
    

def playerInput(event):
    global lives
    global streak
    global score
    computerChoice = random.choice(rpsArray)
    if 450 < event.y < 550:
        if 225 < event.x < 325:
            colouredRect = canvasOne.create_rectangle(225,450,325,550, fill = 'LightBlue')
            colouredPaper = canvasOne.create_text(275, 500, text = 'Paper', font = ('Avenir Next', 20))
            canvasOne.delete(rps)
            window.update()
            time.sleep(0.166666666)
            canvasOne.delete(colouredRect)
            canvasOne.delete(colouredPaper)
            playerChoiceText = canvasOne.create_text(275,150, text = 'You chose Paper', font = ('Avenir Next', 20))
            computerChoiceText = canvasOne.create_text(275,200, text = 'The computer chose: '+computerChoice, font = ('Avenir Next', 20))
            if computerChoice == 'Rock':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpsScreen)
            canvasOne.pack()
        elif 75 < event.x < 175:
            colouredRect = canvasOne.create_rectangle(75,450,175,550, fill = 'Pink')
            colouredRock = canvasOne.create_text(125, 500, text = 'Rock', font = ('Avenir Next', 20))
            canvasOne.delete(rps)
            window.update()
            time.sleep(0.166666666)
            canvasOne.delete(colouredRect)
            canvasOne.delete(colouredRock)
            playerChoiceText = canvasOne.create_text(275,150, text = 'You chose Rock', font = ('Avenir Next', 20))
            computerChoiceText = canvasOne.create_text(275,200, text = 'The computer chose: '+computerChoice, font = ('Avenir Next', 20))
            if computerChoice == 'Rock':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpsScreen)
            canvasOne.pack()
        elif 375 < event.x < 475:
            colouredRect = canvasOne.create_rectangle(375,450,475,550, fill = 'LightGreen')
            colouredScissors = canvasOne.create_text(425, 500, text = 'Scissors', font = ('Avenir Next', 20))
            canvasOne.delete(rps)
            window.update()
            time.sleep(0.166666666)
            canvasOne.delete(colouredRect)
            canvasOne.delete(colouredScissors)
            playerChoiceText = canvasOne.create_text(275,150, text = 'You chose Scissors', font = ('Avenir Next', 20))
            computerChoiceText = canvasOne.create_text(275,200, text = 'The computer chose: '+computerChoice, font = ('Avenir Next', 20))
            if computerChoice == 'Rock':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                lives = lives - 1
                streak = 0
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpsScreen)
            canvasOne.pack()
    elif 475 < event.x < 525:
        if 25 < event.y < 75:
            score = 0
            streak = 0
            rpsStart(event)

rpsStart(event)

window.mainloop()
