import random


def game():
    guess = -1
    tries = 0
    number = random.randint(0, 100)
    while guess is not number:
        tries += 1
        while not (0 <= guess <= 100):
            try:
                guess = int(raw_input("Enter a number between 0 and 100: "))
            except ValueError:
                pass
        if guess is number:
            print "You won after %d tries" % tries
            return
        if guess < number:
            print "Your guess is too low"
        if guess > number:
            print "Your guess is too high"
        guess = -1

game()
