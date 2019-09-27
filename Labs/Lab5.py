import random

guessesTaken = 0
import time


print('Welcome! What is your name?')
myName = input()

number = random.randint(1,15)
print('Well, ' + myName + ', Guess a number between 1 and 15, you have 5 guesses.Good luck!')

time.sleep(1)

while guessesTaken <5:
  print(' Guess a number.')
  guess = input()
  guess = int(guess)

  guessesTaken = guessesTaken + 1
  if guess < number:
    print('Your guess is too low.')
  if guess > number:
    print('Your guess is too high.')
  if guess == number:
    break
if guess == number:
  guessesTaken = str(guessesTaken)
  print('Congrats, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
  number = str(number)
  print('Failed. The number I was thinking of was ' + number)
