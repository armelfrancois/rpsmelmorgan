import random
import time
score = 0
lives = 3
counter = 0
originalLives = 0
streak = 0
originalStreak = 0
rpsArray = ['rock', 'paper', 'scissors']
'rock' > 'scissors'
'scissors' > 'paper'
'paper' > 'rock'

def menu(lives, originalLives):
	print('Welcome to Rock, Paper, Scissors!')
	playerName = input('Please enter your name: ')
	print('Hello ' + playerName + '!')
	while True:
		print('If you wish to play the game, press 1')
		time.sleep(0.7)
		print('If you wish to see the instructions, press 2')
		time.sleep(0.7)
		print('If you wish to see the high scores, press 3')
		time.sleep(0.7)
		print('To change the difficulty, press 4')
		menuChoice = int(input('Please take your choice: '))
		if menuChoice == 1:
			print('Good Luck ' + playerName + '!\n')
			time.sleep(1)
			game(playerName, lives, score, counter, originalLives, streak, originalStreak)
			break
		elif menuChoice == 2:
			print('You have 5 lives in "easy", 3 in "medium" and 1 in "hard".')
			print('Each time you loose, you loose a life. It is game over when your reach 0')
			print('You gain 3 points if you win, and one point if you draw.')
			print('You gain a new life by getting three wins in a row.')
			print('In the final version, your score will be saved in a .txt file.\n')
			time.sleep(10)
			continue
		elif menuChoice == 3:
			print('Not coded for yet')
		elif menuChoice == 4:
			while True:
				difficulty = input('Would you like "easy", "medium" or "hard"? ')
				if difficulty == 'easy':
					lives == 5
					originalLives == 5
					print('Difficulty level set! \n')
					time.sleep(0.7)
					break
				elif difficulty == 'medium':
					print('Difficulty level set! \n')
					time.sleep(0.7)
					originalLives == 3
					break
				elif difficulty == 'hard':
					lives == 1
					originalLives == 1
					print('Difficulty level set! \n')
					time.sleep(0.7)
					break
				else:
					print('Please choose a valid difficulty level!')
					continue
			continue
		else:
			print('Please make a valid choice!')
			continue

def game(playerName, lives, score, counter, originalLives, streak, originalStreak):
	while True:
		if lives > 0:
			print(' ')
			playerChoice = input('Do you choose rock paper or scissors? ')
			computerChoice = random.choice(rpsArray)
			while True:
				if playerChoice == 'rock' or 'paper' or 'scissors':
					break
				else:
					print('Please make a valid choice!')
					continue
			print('The computer chose ' + computerChoice + '...')
			time.sleep(0.5)
			while streak > originalStreak:
				streak == originalStreak - originalStreak + streak
				break
			continue
			while computerChoice == playerChoice:
				print('Draw')
				score = score + 1
				continue
			while playerChoice == 'rock' and computerChoice == 'scissors':
				print('You Win!')
				score = score + 3
				counter = counter + 1
				streak = streak + 1
				continue
			while playerChoice == 'rock' and computerChoice == 'paper':
				print('You Loose!')
				lives = lives - 1
				continue
			while playerChoice == 'scissors' and computerChoice == 'paper':
				print('You Win!')
				score = score + 3
				counter = counter + 1
				streak = streak + 1
				continue
			while playerChoice == 'scissors' and computerChoice == 'rock':
				print('You Loose!')
				lives = lives - 1
				continue
			while playerChoice == 'paper' and computerChoice == 'rock':
				print('You Win!')
				score = score + 3
				counter = counter + 1
				streak = streak + 1
				continue
			while playerChoice == 'paper' and computerChoice == 'scissors':
				print('You Loose!')
				lives = lives - 1
				continue
			if counter == 3:
				lives = lives + 1
				counter == counter - counter
			time.sleep(0.8)
			game(playerName, lives, score, counter, originalLives, streak, originalStreak)
			continue
		elif lives == 0:
			scoreString = str(score)
			winningStreak = str(originalStreak)
			print('Bad Luck! GAME OVER')
			print('You got a score of: ' + scoreString + ' points!')
			time.sleep(0.5)
			print('Your highest winning streak was: ' + winningStreak + '!\n')
			time.sleep(1)
			print(' ')
			print('To play again, press 1')
			time.sleep(0.7)
			print('To see the high scores, press 2')
			time.sleep(0.7)
			print('To return to the menu, press 3')
			time.sleep(0.7)
			while True:
				score == 0
				gameOverChoice = int(input('Please make your choice: '))
				if gameOverChoice == 1:
					lives == (lives - lives) + originalLives
					time.sleep(1)
					print('Good luck ' + playerName + '!')
					game(playerName, lives, score, counter, originalLives, streak, originalStreak)
				elif gameOverChoice == 2:
					print('Not coded for yet')
				elif gameOverChoice == 3:
					lives == (lives - lives) + originalLives
					time.sleep(1)
					print(' \n')
					menu(lives, originalLives)
				else:
					print('Please make a valid choice!')
					continue
				break
				
menu(lives, originalLives)
