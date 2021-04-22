from turtle import Screen


def setup_window():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def check_keys(screen, snake):
    screen.onkeypress(fun=snake.up, key="Up")
    screen.onkeypress(fun=snake.down, key="Down")
    screen.onkeypress(fun=snake.left, key="Left")
    screen.onkeypress(fun=snake.right, key="Right")
    screen.onkeypress(fun=screen.bye, key="Escape")


def check_food_collision(snake, food, scoreboard):
    if snake.head.distance(food) < 1:
        food.refresh()
        scoreboard.increase_score()
        # snake.append()
        snake.extend()


def check_wall_collision(snake, scoreboard):
    if snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        return False
    return True


def check_body_collision(snake, scoreboard):
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            return False
    return True