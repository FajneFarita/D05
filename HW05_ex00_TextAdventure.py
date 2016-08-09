#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0, name):
    print("{} walks through the door to see a dimly lit hallway.".format(name))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room(name):
    print("This room is full of gold.  How much does {} takes?".format(name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {} is not greedy, {} wins!".format(name, name))
        exit(0)
    else:
        dead("{} greedy goose!".format(name))


def bear_room(name):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(name))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or "honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or "door" and bear_moved:
            gold_room(name)
        else:
            print("I got no idea what that means.")


def cthulhu_room(name):
    print("Here {} sees the great evil Cthulhu.".format(name))
    print("He, it, whatever stares at {} and {} goes insane.".format(name, name))
    print("Does {} flees for life or eats own head?".format(name))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        infinite_stairway_room(name)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    username = input("What's your name? ")
    print("{} is in a dark room.".format(username))
    print("There is a door to the right and to the left.")
    print("Which one does {} takes?".format(username))

    next = input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    else:
        dead("{} stumbles around the room until starves.".format(username))

if __name__ == '__main__':
    main()
