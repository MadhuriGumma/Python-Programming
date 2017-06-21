import random

guessesTaken = 0
print('Hello! Guess the number I am thinking. It is between 1 to 10')


number = random.randint(1, 10)


while guessesTaken < 5:

    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Congrats! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
     number = str(number)
     print('Nope. The number I was thinking of was ' + number)