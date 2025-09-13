# make a number randomly between 1 to 3
# ask user to write a number between 1 to 3
# if number is matchign prnt matched
# else print number didnt match

from random import randint

computer = randint(1,3) # make a random number between 1 to 3
user = int(input("please enter a nuber btw 1 to 3:")) # it will ask user to enter a number between 1 to 3

if user == computer: # if user and computer equal mean amtch
    print("matched")
else:
    print("did not match")