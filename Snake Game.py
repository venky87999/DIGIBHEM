"Snake Game"
import pygame
import sys
import time
import random
snake_speed=12
# creating frame with required size
X_axis=720
Y_axis=480
pygame.init()
# Establishing game window
pygame.display.set_caption('Snake Game')
game_window=pygame.display.set_mode((X_axis,Y_axis))
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
#time
Clock=pygame.time.Clock()
# creating varibles for game
snake_pos=[100,50]
snake_body=[[100,50],[100-10,50],[100-(2*10),50]]
food_pos=[random.randrange(1,(X_axis//10))*10,random.randrange(1,(Y_axis//10))*10]
food_s=True
direction='RIGHT'
change_to=direction
score=0
# Score
def show_score(choice,color,font,size):
    score_font=pygame.font.SysFont(font,size)
    score_surface=score_font.render('Score : '+str(score),True,color)
    score_rect=score_surface.get_rect()
    if choice==1:
        score_rect.midtop=(X_axis/10,15)
    else:
        score_rect.midtop=(X_axis/2,Y_axis/1.25)
    game_window.blit(score_surface,score_rect)
# Game Over condition
def game_over():
    my_font=pygame.font.SysFont('times new roman',90)
    game_over_surface=my_font.render('GAME OVER',True,red)
    game_over_rect=game_over_surface.get_rect()
    game_over_rect.midtop=(X_axis/2,Y_axis/4)
    game_window.fill(black)
    game_window.blit(game_over_surface,game_over_rect)
    show_score(0,red,'times',20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#game main function starts here
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif i.type==pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if i.key==pygame.K_UP or i.key==ord('w'):
                change_to='UP'
            if i.key==pygame.K_DOWN or i.key==ord('s'):
                change_to = 'DOWN'
            if i.key==pygame.K_LEFT or i.key==ord('a'):
                change_to = 'LEFT'
            if i.key==pygame.K_RIGHT or i.key==ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if i.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

#making game in one direction only
    if change_to=='UP' and direction!='DOWN':
        direction='UP'
    if change_to=='DOWN' and direction!='UP':
        direction='DOWN'
    if change_to=='LEFT' and direction!='RIGHT':
        direction='LEFT'
    if change_to=='RIGHT' and direction !='LEFT':
        direction='RIGHT'

    # Moving the snake
    if direction=='UP':
        snake_pos[1]-=10
    if direction=='DOWN':
        snake_pos[1]+=10
    if direction=='LEFT':
        snake_pos[0]-=10
    if direction=='RIGHT':
        snake_pos[0]+=10
# snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        score+=1
        food_s=False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_s:
        food_pos=[random.randrange(1,(X_axis//10))*10,random.randrange(1,(Y_axis//10))*10]
    food_s=True
    #back ground window
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window,green,pygame.Rect(pos[0],pos[1],10,10))
    # Snake food
    pygame.draw.rect(game_window,white,pygame.Rect(food_pos[0],food_pos[1], 10, 10))

    # Game conditions for completion
    if snake_pos[0] < 0 or snake_pos[0]>X_axis-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1]>Y_axis-10:
        game_over()
        #snake body touching itself
    for block in snake_body[1:]:
        if snake_pos[0]==block[0] and snake_pos[1]==block[1]:
            game_over()
    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    Clock.tick(snake_speed)