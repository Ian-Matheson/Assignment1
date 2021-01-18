from karel.stanfordkarel import *

def main():
    all_towers()

def all_towers():
    for i in range(4):
        build_tower()
        if no_beepers_present():
            put_beeper()
            go_back()
        else:
            go_back()
        turn_left()
        if front_is_clear():
            next_tower()
        else:
            turn_left()

def build_tower():
    turn_left()
    for i in range(4):
        if beepers_present():
            move()
        else:
            put_beeper()
            move()

def go_back():
    turn_around()
    for i in range(4):
        move()

def next_tower():
    for i in range(4):
        move()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
