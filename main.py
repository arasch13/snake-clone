from snake import Snake
from food import Food
from score import Scoreboard
from help_functions import *
import time

# prepare screen
screen = setup_window()

# create scoreboard
scoreboard = Scoreboard()

# create snake
snake = Snake()

# create food
food = Food()

# listen to events
screen.listen()

# run game
game_is_on = True
while game_is_on:
    check_keys(screen, snake)
    snake.move()
    check_food_collision(snake, food, scoreboard)
    game_is_on = check_wall_collision(snake, scoreboard)
    game_is_on = check_body_collision(snake, scoreboard)
    screen.update()
    time.sleep(0.1)


screen.exitonclick()