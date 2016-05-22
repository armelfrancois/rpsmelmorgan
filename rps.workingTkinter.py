# Rock Paper Scissors

from tkinter import *
import random
import time
import sys

window = Tk()
window.geometry('550x700')
window.wm_title('Rock Paper Scissors')
rpsArray = ['Rock', 'Paper', 'Scissors']

canvasOne = Canvas(window, width = 550, height = 700)
canvasOne.pack()

def rpsScreen():
    global rps
    canvasOne.delete(ALL)
    firstRect = canvasOne.create_rectangle(225,450,325,550, fill = 'Blue')
    secondRect = canvasOne.create_rectangle(75,450,175,550, fill = 'Red')
    thirdRect = canvasOne.create_rectangle(375,450,475,550, fill = 'Green')
    rock = canvasOne.create_text(125, 500, text = 'Rock', font = ('Avenir Next', 20))
    paper = canvasOne.create_text(275, 500, text = 'Paper', font = ('Avenir Next', 20))
    scissors = canvasOne.create_text(425, 500, text = 'Scissors', font = ('Avenir Next', 20))
    rps = canvasOne.create_text(275, 250, text = 'Rock Paper Or Scissors?', justify = CENTER, font = ('Avenir Next', 30))
    canvasOne.bind('<Button-1>', playerInput)
    canvasOne.pack

def playerInput(event):
    computerChoice = random.choice(rpsArray)
    if 450 < event.y < 550:
        if 225 < event.x < 325:
            print('You pressed')
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
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You lost', font = ('Avenir Next', 30))
            window.update()
            time.sleep(3)
            rpsScreen()
        elif 75 < event.x < 175:
            print('You pressed')
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
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
            window.update()
            time.sleep(3)
            rpsScreen()
        elif 375 < event.x < 475:
            print('You pressed')
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
            elif computerChoice == 'Paper':
                resultText = canvasOne.create_text(275,300, text = 'You won', font = ('Avenir Next', 30))
            elif computerChoice == 'Scissors':
                resultText = canvasOne.create_text(275,300, text = 'You drew', font = ('Avenir Next', 30))
            window.update()
            time.sleep(3)
            rpsScreen()
            
            
            

rpsScreen()

window.mainloop()
