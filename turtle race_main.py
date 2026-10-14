import turtle
import random
import time

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'brown'] 

def num_of_racers():
    racers = 0
    while True:
        racers = input('How many racers are there (2-10)? ')
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print('Please enter a number between 2 and 10.')
        else:
            print('Please enter a valid number.')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randint(1, 10)
            racer.forward(distance)
            if racer.ycor() >= HEIGHT//2 - 20:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.goto(-WIDTH//2 + (i+1)*spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def screen_turtle():
    screen = turtle.Screen()
    WIDTH , HEIGHT = 500,500
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')
    screen.bgcolor('lightgreen')
    

def main():
    screen = screen_turtle()
    print(screen)
    racers = num_of_racers()
    print(f'There are {racers} racers in the race.')

    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print(f'The winner is {winner}')
    time.sleep(5)
main()