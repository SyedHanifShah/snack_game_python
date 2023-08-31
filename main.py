from turtle import Turtle, Screen
import time
from snack import Snack
from food import Food
from score_board import Scoreboard

my_color = ["red", "blue", "green", "black", "purple", "green yellow", "firebrick", "cornflower blue",
            "medium violet red", "orchid", "medium slate blue", "lavender", "saddle brown", "deep pink", "orange",
            "salmon", "orange red", "magenta"]

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.title("The Snack Game")

snack = Snack()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snack.up, "Up")
my_screen.onkey(snack.down, "Down")
my_screen.onkey(snack.left, "Left")
my_screen.onkey(snack.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snack.move()

    if snack.segment[0].distance(food) < 15:
        food.refresh()
        snack.extend()
        scoreboard.increase_score()

    if snack.segment[0].xcor() > 280 or snack.segment[0].xcor() < -280 or snack.segment[0].ycor() > 280 or snack.segment[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snack.segment[1:]:
        if snack.segment[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


my_screen.exitonclick()
