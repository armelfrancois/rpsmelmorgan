# Rock Paper Scissors

from tkinter import *
import random
import time
import sys

#event is useless, the code doesn't work without it though so...
event = 0

window = Tk()
window.geometry('550x650')
window.wm_title('Rock Paper Scissors')
rpsArray = ['Rock', 'Paper', 'Scissors']

lives = 3
score = 0
streak = 0
hardHighscore = 0
mediumHighscore = 0
easyHighscore = 0
difficulty = 'easy'

canvasOne = Canvas(window, width = 550, height = 650)
canvasOne.configure(background = 'white')
canvasOne.pack()

backgroundImage = PhotoImage(file = 'background.png')

homeButton = PhotoImage(file = 'homeButton.png')
heartSymbol = PhotoImage(file = 'heartSymbol.png')
rockSymbol = PhotoImage(file = 'rock.png')
paperSymbol = PhotoImage(file = 'paper.png')
scissorsSymbol = PhotoImage(file = 'scissors.png')
rock2Symbol = PhotoImage(file = 'rock2.png')
paper2Symbol = PhotoImage(file = 'paper2.png')
scissors2Symbol = PhotoImage(file = 'scissors2.png')

def rpsStart(event):
    canvasOne.delete(ALL)
    background = canvasOne.create_image(275,350, image = backgroundImage)
    welcome = canvasOne.create_text(275,250, text = 'Play', font = ('Avenir Next', 40))
    highscore = canvasOne.create_text(275, 450, text = 'Highscores', font = ('Avenir Next', 25))
    settings = canvasOne.create_text(275, 550, text = 'Settings', font = ('Avenir Next', 25))
    canvasOne.bind('<Button-1>', menuChoice)
    canvasOne.pack()

def showHighscores():
    global highscore
    global hardHighscore
    global mediumHighscore
    global easyHighscore
    global difficulty
    canvasOne.delete(ALL)
    background = canvasOne.create_image(275,350, image = backgroundImage)
    showScore = canvasOne.create_text(275,250, text = 'In this mode you have stood:', font = ('Avenir Next', 25))
    if difficulty == 'easy':
        showScoreTwo = canvasOne.create_text(275,300, text = easyHighscore, font = ('Avenir Next', 30))
    elif difficulty == 'medium':
        showScoreTwo = canvasOne.create_text(275,300, text = mediumHighscore, font = ('Avenir Next', 30))
    elif difficulty == 'hard':
        showScoreTwo = canvasOne.create_text(275,300, text = hardHighscore, font = ('Avenir Next', 30))
    showScoreThree = canvasOne.create_text(275,350, text = 'rounds against the computer', font = ('Avenir Next', 25))
    canvasOne.unbind('<Button-1>')
    canvasOne.pack()
    window.update()
    canvasOne.bind('<Button-1>', rpsStart)
    canvasOne.pack()

def settings():
    canvasOne.delete(ALL)
    background = canvasOne.create_image(275,350, image = backgroundImage)
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
    global score
    global difficulty
    if event.y < 300:
        difficulty = 'hard'
        score = 0
        lives = 1
    elif event.y > 400:
        difficulty = 'easy'
        score = 0
        lives = 3
    elif 300 < event.y < 400:
        difficulty = 'medium'
        score = 0
        lives = 2
    rpsStart(event)

def menuChoice(event):
    if 400 < event.y < 500:
        showHighscores()
    elif 500 < event.y < 600:
        settings()
    else:
        rpsScreen(event)

def rpsScreen(event):
    global rps
    global lives
    global score
    global highscore
    global rock
    global paper
    global scissors
    global easyHighscore
    global mediumHighscore
    global hardHighscore
    global difficulty
    canvasOne.unbind('<Button-1>')
    window.update()
    canvasOne.delete(ALL)
    homeRect = canvasOne.create_image(500,50, image = homeButton)
    rock = canvasOne.create_image(125,550, image = rockSymbol)
    paper = canvasOne.create_image(275,550, image = paperSymbol)
    scissors = canvasOne.create_image(425,550, image = scissorsSymbol)
    rps = canvasOne.create_text(275, 250, text = 'Rock Paper Or Scissors?', justify = CENTER, font = ('Avenir Next', 30))
    canvasOne.bind('<Button-1>', playerInput)
    canvasOne.pack
    if lives == 0:
        canvasOne.delete(ALL)
        youLost = canvasOne.create_text(275, 250, text = 'YOU LOST', font = ('Avenir Next',30))
        lives = 3
        if difficulty == 'easy':
            if easyHighscore < score:
                easyHighscore = score
        elif difficulty == 'medium':
            if mediumHighscore < score:
                mediumHighscore = score
        elif difficulty == 'hard':
            if hardHighscore < score:
                hardHighscore = score
        score = 0
        canvasOne.unbind('<Button-1>')
        canvasOne.pack()
        window.update()
        canvasOne.bind('<Button-1>', rpsStart)
        canvasOne.pack()
    elif lives == 1:
        firstHeart = canvasOne.create_image(50,50, image = heartSymbol)
    elif lives == 2:
        firstHeart = canvasOne.create_image(50,50, image = heartSymbol)
        secondHeart = canvasOne.create_image(125,50, image = heartSymbol)
    elif lives == 3:
        firstHeart = canvasOne.create_image(50,50, image = heartSymbol)
        secondHeart = canvasOne.create_image(125,50, image = heartSymbol)
        thirdHeart = canvasOne.create_image(200,50, image = heartSymbol)
    else:
        lives == 3
        firstHeart = canvasOne.create_image(50,50, image = heartSymbol)
        secondHeart = canvasOne.create_image(125,50, image = heartSymbol)
        thirdHeart = canvasOne.create_image(200,50, image = heartSymbol)
    

def playerInput(event):
    global lives
    global streak
    global score
    global rock
    global paper
    global scissors
    computerChoice = random.choice(rpsArray)
    if 500 < event.y < 600:
        if 225 < event.x < 325:
            canvasOne.delete(paper)
            smallPaper = canvasOne.create_image(275,550, image = paper2Symbol)
            canvasOne.delete(rps)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallPaper)
            paper = canvasOne.create_image(275,550, image = paperSymbol)
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
            canvasOne.delete(rock)
            smallRock = canvasOne.create_image(125,550, image = rock2Symbol)
            canvasOne.delete(rps)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallRock)
            rock = canvasOne.create_image(125,550, image = rockSymbol)
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
            canvasOne.delete(scissors)
            smallScissors = canvasOne.create_image(425,550, image = scissors2Symbol)
            canvasOne.delete(rps)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallScissors)
            scissors = canvasOne.create_image(425,550, image = scissorsSymbol)
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
            rpsStart(event)

rpsStart(event)

window.mainloop()
