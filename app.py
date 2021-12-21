# colour = raw_input("Enter a colour ")
# sound = raw_input("Enter a sound ")
# place = raw_input("Enter a place ")

# print("You are a " + place)
# print("The place is a " + sound)
# print("That sound is a " + colour)

# my_list = [1,2,4,6,7]
# add_me = [8,9,10]
# my_list.extend(add_me)
# my_list.append(12)
# print(my_list)

# coordinates = (4,5, 'abc')
# print(coordinates[0])

# def sayHi(a):
#     print('hi')
#     print(a)

#     print('why')

#     return 'the return'


# def isTrue(boolean):
#     if (boolean): return 'true'
#     else:
#         return 'false'

# print(isTrue(False))

# dan = 101

# if (dan > 18 and dan < 15): print('danny')

# if (dan > 5) and not (dan == 100):
#     print('greater than 5')
# elif (dan < 20):
#     print('less than 20')

# if not (dan == 100):
#     print('not equal to 100')

# def calculator(a, operator, b):
#     if(operator == '*'):
#         return a * b
#     if(operator == '-'):
#         return a - b
#     if(operator == '+'):
#         return a + b
#     if(operator == '/'):
#         return a / b


# print(calculator(1, '/', 2))

# myDictionary = {
#     'dan': 18,
#     'han' : 13
# }

# name = 'dan'

# print(myDictionary)

# int = 10

# while int >= 0:
#     print(int)
#     int -= 1

import random


names = ['dan', 'han', 'gran', 'ted']


def guessGame(list):
    randIdx = random.randint(0, len(list) - 1)
    selectedValue = list[randIdx]
    gamePlaying = True
    attemps = 0

    print('Guess from one of the follwing ' + list)

    while(gamePlaying):
        guess = raw_input('Guess a the random value: ')
        attemps += 1
        if (guess == selectedValue):
            gamePlaying = False
            print('You guessed ' + guess + ' and the value was ' + selectedValue)
            print('It took you ' + str(attemps) + ' attempts!')
            return
        else:
            print('Your guess is incorrect')
            print('It has taken you ' + str(attemps) + ' attempts, and you still haven\'t got it :(')
    return


guessGame(names)
