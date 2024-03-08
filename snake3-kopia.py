#Import
import pygame as pg
from random import randrange


WINDOW = 1000
TILE_SIZE = 50

RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1

segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110

food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)

clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

#This code allows you to control the snake with some rules added so you can't cheat by going from upwards to downwards in a single click.
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
    screen.fill('black')
   #check borders and selfeating, this code makes it so that there are death berriers and that if you go through yourself you die and lose the game.
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
    # This allows the food to work. When you consume it you get longer and it teleports to a random location.
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    # This code draws the red colored square food that you can eat.
    pg.draw.rect(screen, 'red', food)
    # This code draws the snake itself.
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
   # This code allows the snake to exist, without this code it won't move around.
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    # This code allows the program to be shown on the screen and also puts an fps cap so it doesn't unnecessarily run at a higher fps for no reason.
    pg.display.flip()
    clock.tick(60)

#NOTE: You should know that like everyone else I used help from youtube and sometimes chatgpt to write this pygame.