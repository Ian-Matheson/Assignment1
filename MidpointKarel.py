from karel.stanfordkarel import * 

def main():
    fill_map()
    place_goal()
    prep_clean()
    clean_up()

def fill_map():
    square1()
    reposition()
    while no_beepers_present():
        one_line2()
    turn_around()
    move()

def square1():
    for i in range(4):
        one_line1()
        turn_left()

def one_line1():
    while front_is_clear():
        put_beeper()
        move()

def square2():
    one_line2()
    reposition()

def one_line2():
    while no_beepers_present():
        put_beeper()
        move()
    turn_left()
    reposition()

def place_goal():
    while front_is_clear():
        move()
    put_beeper()

def clean_up():
    clean_square1()
    reposition()
    while beepers_present():
        clean_one_line2()

def clean_square1():
    for i in range(4):
        clean_one_line1()
        turn_left()

def clean_one_line1():
    while front_is_clear():
        pick_beeper()
        move()

def clean_square2():
    one_line2()
    reposition()

def clean_one_line2():
    while beepers_present():
        pick_beeper()
        move()
    turn_left()
    reposition()

def prep_clean():
    turn_right()
    while front_is_clear():
        move()
    turn_around()

def reposition():
    move()
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
