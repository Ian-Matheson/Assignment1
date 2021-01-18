from karel.stanfordkarel import *

def main():
    for c in range(3):
        paint_building()
        reset()

def paint_building():
    for i in range(3):
        paint_1()
        move()

def paint_1():
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()

def reset():
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
