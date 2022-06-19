from cmu_graphics import *
import random

AI_mode = False


def path_finder():
    pass


def game_over():
    app.background = "black"
    food.fill = "black"
    Label("Game over", 200, 200, fill="white")
    Label("Score: ", 200, 225, fill="white")
    Label(score.value, 225, 225, fill="white")
    app.stop()


def generate_food():
    food.centerX = random.randrange(block, width, block) - block / 2
    food.centerY = random.randrange(block, height, block) - block / 2


def check_collision():
    if snake.centerX >= width or snake.centerX <= 0 or snake.centerY >= height or snake.centerY <= 0:
        game_over()
    for i in range(len(snake.body) - 1):
        if snake.centerX == snake.body[i].centerX and snake.centerY == snake.body[i].centerY:
            game_over()


def get_food():
    snake.body.insert(0, Rect(snake.centerX - block / 2, snake.centerY - block / 2, block, block))
    score.value += 1
    generate_food()


def move_head():
    if snake.direction == "right":
        snake.centerX += block
    elif snake.direction == "left":
        snake.centerX -= block
    elif snake.direction == "up":
        snake.centerY -= block
    elif snake.direction == "down":
        snake.centerY += block
    snake.direction_flag = False


def onKeyPress(key):
    # change direction
    if not snake.direction_flag:
        if key == "right" or key == "d":
            if snake.direction != "left" and snake.direction != "right":
                snake.direction = "right"
                snake.direction_flag = True
        if key == "left" or key == "a":
            if snake.direction != "right" and snake.direction != "left":
                snake.direction = "left"
                snake.direction_flag = True
        if key == "down" or key == "s":
            if snake.direction != "up" and snake.direction != "down":
                snake.direction = "down"
                snake.direction_flag = True
        if key == "up" or key == "w":
            if snake.direction != "down" and snake.direction != "up":
                snake.direction = "up"
                snake.direction_flag = True


def move_snake():
    for i in range(len(snake.body) - 1, 0, -1):
        snake.body[i].centerX, snake.body[i].centerY = snake.body[i - 1].centerX, snake.body[i - 1].centerY
    snake.body[0].centerX, snake.body[0].centerY = snake.centerX, snake.centerY


def get_x_direction(x_dif):
    direction = ""
    if x_dif == 0:
        return direction
    if x_dif > 0 and snake.direction != "left":
        direction = "right"
    elif snake.direction != "right":
        direction = "left"
    return direction


def get_y_direction(y_dif):
    direction = ""
    if y_dif == 0:
        return direction
    if y_dif > 0 and snake.direction != "up":
        direction = "down"
    elif snake.direction != "down":
        direction = "up"
    return direction


def AI():
    x_dif = food.centerX - snake.centerX
    y_dif = food.centerY - snake.centerY
    x_direction = get_x_direction(x_dif)
    y_direction = get_y_direction(y_dif)
    if not snake.direction_flag:
        if x_direction != "":
            snake.direction = x_direction
        else:
            snake.direction = y_direction
        snake.direction_flag = True


def onStep():
    if AI_mode:
        AI()
    move_head()
    check_collision()
    # check if collide with food
    if snake.centerX == food.centerX and snake.centerY == food.centerY:
        get_food()
    else:
        move_snake()


if __name__ == '__main__':
    # speed of game
    app.stepsPerSecond = 20

    # snake size
    block = 10
    width, height = 400, 400

    # init food
    food = Rect(200, 50, block, block, fill="red")
    generate_food()

    # init snake
    snake = Rect(100, 50, block, block)
    snake.direction = "right"
    snake.direction_flag = False
    snake.body = [Rect(100, 50, block, block), Rect(90, 50, block, block), Rect(80, 50, block, block)]

    # score
    score = Label(0, 10, 10)

    cmu_graphics.run()
