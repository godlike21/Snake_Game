import pygame
import sys
from pygame.math import Vector2
import random

#starting pygame
pygame.init()

#to make the screen more flexible/dividing the screen
cell_size = 32
cell_number = 18

#creating screen
screen = pygame.display.set_mode((cell_size * cell_number , cell_size * cell_number))

#creating screen title
pygame.display.set_caption("Snake Game  @sanjok_mangrati")

#fetching clock func. to use later
clock = pygame.time.Clock()

#creating snake
class SNAKE:

    #method for snake position
    def __init__(self):
        self.body = [Vector2(5,10) ,Vector2(4,10) , Vector2(3,10)]   #snake body
        self.direction = Vector2(1,0)       #direction
        self.new_block = False   #boolean for new block condition default to false

    #method to draw snake
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x*cell_size) , int(block.y*cell_size) , cell_size , cell_size)  #creating snake body rect
            pygame.draw.rect(screen , (255,255,0) , snake_rect)  #to draw snake

    #method to move snake
    def snake_move(self):
        #to add a block to body
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, self.body[0] + self.direction)
            self.body = body_copy[:]  # to update snake position
            self.new_block = False

        else:
            body_copy = self.body[ :-1]
            body_copy.insert(0,self.body[0] + self.direction)
            self.body = body_copy[:]    #to update snake position

    #method that checks to add block
    def add_block(self):
        self.new_block = True



#creating fruit for the snake
class FRUIT:

    def __init__(self):
        self.randomize()


    #method to draw fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect((int(self.pos.x*cell_size) , int(self.pos.y*cell_size) , cell_size , cell_size))  #creating rectangle
        pygame.draw.rect(screen , (210 , 60 , 80) , fruit_rect)   # to draw the rectangle

    # method to define postion
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)  # to randomize x coordinate
        self.y = random.randint(0, cell_number - 1)  # to randomize y coordinate

        self.pos = Vector2(self.x, self.y)  # using 2D vector to store the x and y position of fruit


#creating main game logic
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    #method to trigger snake movement
    def update(self):
        self.snake.snake_move()  #using snake_move from self.snake from SNAKE
        self.HF_collision()
        self.check_collision()

    #method for drawing elements on screen
    def draw_elements(self):
        self.fruit.draw_fruit()  # using draw_fruit from self.fruit from class FRUIT
        self.snake.draw_snake()  # using draw_snake from self.snake from class SNAKE

    #method to check snake head and fruit collision
    def HF_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()   #to randomize fruit position when head block = fruit pos
            self.snake.add_block()   #to add block to snake body

    #method to check collision
    def check_collision(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number :  #checking snake in screen or not/snake hit wall
            self.game_over()

        for block in self.snake.body[1:]:   #checking collision with itself
            if block == self.snake.body[0]:
                self.game_over()


    #to check game over
    def game_over(self):
        pygame.quit()  # to quit pygame
        sys.exit()



#storing MAIN in var
main_game = MAIN()

#creating custom event and storing in variable
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE , 150)  #setting a timer to trigger event at certain interval



#main/game loop
while True:

    #checking for possible events
    for event in pygame.event.get():

        #checking for event type exit/quit
        if event.type == pygame.QUIT:
            pygame.quit()   #to quit pygame
            sys.exit()      #to make sure every process stops

        #checking for custom event/i.e SCREEN_UPDATE in this case
        if event.type == SCREEN_UPDATE:
             main_game.update()  #using update from MAIN

        #checking for event type key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:  #to check snake not moving down
                    main_game.snake.direction = Vector2(0,-1)  #for up movement

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:  # to check snake not moving up
                    main_game.snake.direction = Vector2(0,1)   #for down movement

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:  # to check snake not moving right
                    main_game.snake.direction = Vector2(-1,0)  #for left movement

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:  # to check snake not moving left
                    main_game.snake.direction = Vector2(1,0)   #for right movement



    screen.fill((64,224,208))  #for background color

    main_game.draw_elements()  #using draw_elements from MAIN
    pygame.display.update()  #updating the display

    #framerate of the game/the speed at which while loop runs
    clock.tick(60)















