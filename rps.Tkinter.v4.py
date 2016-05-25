# Rock Paper Scissors

from tkinter import *
import random
import time
import sys
import winsound

#event is useless, the code doesn't work without it though so...
event = 0

#configuring window and canvas
window = Tk()
window.geometry('550x650')
window.wm_title('Rock Paper Scissors')
canvasOne = Canvas(window, width = 550, height = 650)
canvasOne.configure(background = 'white')
canvasOne.pack()

#defining variables
rpsArray = ['Rock', 'Paper', 'Scissors']
rpslsArray = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
lizardNumber = 1
lives = 3
score = 0
streak = 0
hardHighscore = 0
mediumHighscore = 0
easyHighscore = 0
rpslsHighscore = 0
difficulty = 'easy'
first = True
first2 = True

#adding images
backgroundImage = PhotoImage(file = 'background.png')
homeButton = PhotoImage(file = 'homeButton.png')
heartSymbol = PhotoImage(file = 'heartSymbol.png')
rockSymbol = PhotoImage(file = 'rock.png')
paperSymbol = PhotoImage(file = 'paper.png')
scissorsSymbol = PhotoImage(file = 'scissors.png')
rock2Symbol = PhotoImage(file = 'rock2.png')
paper2Symbol = PhotoImage(file = 'paper2.png')
scissors2Symbol = PhotoImage(file = 'scissors2.png')
lizardIcon = PhotoImage(file = 'lizardLogo.png')
lizard2Icon = PhotoImage(file = 'lizardLogo2.png')
lizard3Icon = PhotoImage(file = 'lizardLogo3.png')
lizard4Icon = PhotoImage(file = 'lizardLogo4.png')
lizard5Icon = PhotoImage(file = 'lizardLogo5.png')
lizard6Icon = PhotoImage(file = 'lizardLogo6.png')
lizard7Icon = PhotoImage(file = 'lizardLogo7.png')
lizard8Icon = PhotoImage(file = 'lizardLogo8.png')
lizard9Icon = PhotoImage(file = 'lizardLogo9.png')
lizard10Icon = PhotoImage(file = 'lizardLogo10.png')
lizardSymbol = PhotoImage(file = 'lizard.png')
lizard2Symbol = PhotoImage(file = 'lizard2.png')
paper3Symbol = PhotoImage(file = 'paper3.png')
paper4Symbol = PhotoImage(file = 'paper4.png')
rock3Symbol= PhotoImage(file = 'rock3.png')
rock4Symbol = PhotoImage(file = 'rock4.png')
scissors3Symbol = PhotoImage(file = 'scissors3.png')
scissors4Symbol = PhotoImage(file = 'scissors4.png')
spockSymbol = PhotoImage(file = 'spock.png')
spock2Symbol = PhotoImage(file = 'spock2.png')

def rpsStart(event):
    global first
    global first2
    if first != True:
        winsound.PlaySound('button-3', winsound.SND_FILENAME)
    first = False
    first2 = True
    canvasOne.delete(ALL)
    background = canvasOne.create_image(275,350, image = backgroundImage)
    welcome = canvasOne.create_text(275,250, text = 'Play', font = ('Avenir Next', 40))
    highscore = canvasOne.create_text(275, 450, text = 'Highscores', font = ('Avenir Next', 25))
    settings = canvasOne.create_text(275, 550, text = 'Settings', font = ('Avenir Next', 25))
    canvasOne.bind('<Button-1>', menuChoice)
    canvasOne.pack()

def showHighscores():
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
    winsound.PlaySound('button-3', winsound.SND_ASYNC)
    canvasOne.unbind('<Button-1>')
    canvasOne.pack()
    window.update()
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
    global lizardNumber
    global lizard
    global first2
    if first2 != True:
        winsound.PlaySound('button-9', winsound.SND_FILENAME)
    first2 = False
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
    lizardNumber = random.randint(1,10)
    if lizardNumber == 1:
        lizard = canvasOne.create_image(275,200, image = lizardIcon)
    if lives == 0:
        winsound.PlaySound('button-4', winsound.SND_ASYNC)
        canvasOne.delete(ALL)
        youLost = canvasOne.create_text(275, 250, text = 'YOU LOST', font = ('Avenir Next',30))
        if difficulty == 'easy':
            lives = 3
            if easyHighscore < score:
                easyHighscore = score
        elif difficulty == 'medium':
            lives = 2
            if mediumHighscore < score:
                mediumHighscore = score
        elif difficulty == 'hard':
            lives = 1
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
        print(lives)
        lives = 3
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
    global lizardNumber
    global lizard
    global first2
    if first2 != True:
        winsound.PlaySound('button-9', winsound.SND_ASYNC)
    first2 = False
    if lizardNumber == 1:
        canvasOne.delete(lizard)
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
    elif 225 < event.x < 325:
        if 175 < event.y < 225:
            if lizardNumber == 1:
                first2 = True
                winsound.PlaySound('button-2.wav', winsound.SND_ASYNC)
                lizard1 = canvasOne.create_image(275,350, image = lizardIcon)
                window.update()
                time.sleep(0.1)
                lizard2 = canvasOne.create_image(275,350, image = lizard2Icon)
                window.update()
                time.sleep(0.1)
                lizard3 = canvasOne.create_image(275,350, image = lizard3Icon)
                window.update()
                time.sleep(0.1)
                lizard4 = canvasOne.create_image(275,350, image = lizard4Icon)
                window.update()
                time.sleep(0.1)
                lizard5 = canvasOne.create_image(275,350, image = lizard5Icon)
                window.update()
                time.sleep(0.1)
                lizard6 = canvasOne.create_image(275,350, image = lizard6Icon)
                window.update()
                time.sleep(0.1)
                lizard7 = canvasOne.create_image(275,350, image = lizard7Icon)
                window.update()
                time.sleep(0.1)
                lizard8 = canvasOne.create_image(275,350, image = lizard8Icon)
                window.update()
                time.sleep(0.1)
                lizard9 = canvasOne.create_image(275,350, image = lizard9Icon)
                window.update()
                time.sleep(0.1)
                lizard10 = canvasOne.create_image(275,350, image = lizard10Icon)
                window.update()
                time.sleep(0.1)
                lives = 3
                difficulty = 'rpsls'
                rpslsScreen(event)

def rpslsScreen(event):
    global rps
    global ls
    global lives
    global score
    global rock
    global paper
    global scissors
    global lizard
    global spock
    global rpslsHighscore
    global first2
    if first2 != True:
        winsound.PlaySound('button-9', winsound.SND_ASYNC)
    first2 = False
    canvasOne.unbind('<Button-1>')
    window.update()
    canvasOne.delete(ALL)
    homeRect = canvasOne.create_image(500,50, image = homeButton)
    rock = canvasOne.create_image(125,450, image = rock3Symbol)
    paper = canvasOne.create_image(275,450, image = paper3Symbol)
    scissors = canvasOne.create_image(425,450, image = scissors3Symbol)
    lizard = canvasOne.create_image(200,550, image = lizardSymbol)
    spock = canvasOne.create_image(350,550, image = spockSymbol)
    rps = canvasOne.create_text(275, 250, text = 'Rock Paper Scissors', justify = CENTER, font = ('Avenir Next', 30))
    ls = canvasOne.create_text(275, 300, text = 'Lizard or Spock', justify = CENTER, font = ('Avenir Next', 30))
    canvasOne.bind('<Button-1>', rpslsPlayerInput)
    canvasOne.pack
    if lives == 0:
        winsound.PlaySound('button-4', winsound.SND_ASYNC)
        canvasOne.delete(ALL)
        youLost = canvasOne.create_text(275, 250, text = 'YOU LOST', font = ('Avenir Next',30))
        lives = 3
        if score > rpslsHighscore:
            rpslsHighscore = score
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
        print(lives)
        lives = 3
        firstHeart = canvasOne.create_image(50,50, image = heartSymbol)
        secondHeart = canvasOne.create_image(125,50, image = heartSymbol)
        thirdHeart = canvasOne.create_image(200,50, image = heartSymbol)

def rpslsPlayerInput(event):
    global lives
    global streak
    global score
    global rock
    global paper
    global scissors
    global lizard
    global spock
    global rps
    global ls
    global first2
    if first2 != True:
        winsound.PlaySound('button-9', winsound.SND_ASYNC)
    first2 = False
    computerChoice = random.choice(rpslsArray)
    if 500 < event.y < 600:
        if 150 < event.x < 250:
            canvasOne.delete(lizard)
            smallLizard = canvasOne.create_image(200,550, image = lizard2Symbol)
            canvasOne.delete(rps)
            canvasOne.delete(ls)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallLizard)
            lizard = canvasOne.create_image(200,550, image = lizardSymbol)
            computerChoiceText = canvasOne.create_text(275,200, text = 'The computer chose: '+computerChoice, font = ('Avenir Next', 20))
            if computerChoice == 'Rock':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            elif computerChoice == 'Lizard':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            elif computerChoice == 'Spock':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0  
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpslsScreen)
            canvasOne.pack()
        elif 300 < event.x < 400:
            canvasOne.delete(spock)
            smallSpock = canvasOne.create_image(350,550, image = spock2Symbol)
            canvasOne.delete(rps)
            canvasOne.delete(ls)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallSpock)
            spock = canvasOne.create_image(350,550, image = spockSymbol)
            computerChoiceText = canvasOne.create_text(275,200, text = 'The computer chose: '+computerChoice, font = ('Avenir Next', 20))
            if computerChoice == 'Rock':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
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
            elif computerChoice == 'Lizard':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            elif computerChoice == 'Spcok':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpslsScreen)
            canvasOne.pack()
    elif 400 < event.y < 500:
        if 75 < event.x < 175:
            canvasOne.delete(rock)
            smallRock = canvasOne.create_image(125,450, image = rock4Symbol)
            canvasOne.delete(rps)
            canvasOne.delete(ls)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallRock)
            rock = canvasOne.create_image(125,450, image = rock3Symbol)
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
            elif computerChoice == 'Lizard':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0  
            elif computerChoice == 'Spock':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpslsScreen)
            canvasOne.pack()
        elif 225 < event.x < 325:
            canvasOne.delete(paper)
            smallPaper = canvasOne.create_image(275,450, image = paper4Symbol)
            canvasOne.delete(rps)
            canvasOne.delete(ls)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallPaper)
            spock = canvasOne.create_image(275,450, image = paper3Symbol)
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
            elif computerChoice == 'Lizard':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            elif computerChoice == 'Spock':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpslsScreen)
            canvasOne.pack()
        elif 375 < event.x < 475:
            canvasOne.delete(scissors)
            smallScissors = canvasOne.create_image(425,450, image = scissors4Symbol)
            canvasOne.delete(rps)
            canvasOne.delete(ls)
            window.update()
            time.sleep(0.1)
            canvasOne.delete(smallScissors)
            sscissors = canvasOne.create_image(425,450, image = scissors3Symbol)
            computerChoiceText = canvasOne.create_text(275,200, text = 'The computer chose: '+computerChoice, font = ('Avenir Next', 20))
            if computerChoice == 'Rock':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            elif computerChoice == 'Lizard':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
                streak = streak + 1
                if streak == 3:
                    lives = lives + 1
                    streak = 0
            elif computerChoice == 'Spock':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
                streak = 0
                lives = lives - 1
            score = score + 1
            canvasOne.unbind('<Button-1>')
            canvasOne.pack()
            window.update()
            canvasOne.bind('<Button-1>', rpslsScreen)
            canvasOne.pack()
    elif 475 < event.x < 525:
        if 25 < event.y < 75:
            rpsStart(event)
    
rpsStart(event)

window.mainloop()
