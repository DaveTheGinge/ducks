from random import randint
import pygame
import pgzrun
duck = Actor('duck0')
duck.topright = 0, 10
background = Actor('pasture')
SHELLS = 20
shells_remaining = SHELLS
kills=0
WIDTH = 500
HEIGHT = 700

duck_speed=1
background.topright = WIDTH,0
   
def update():
    global duck_speed
    
    duck.left += duck_speed
    if(duck.image != 'duck_hurt'):
        duck_num=int(duck.image[-1])
        duck_num=(duck_num+1)%6
        duck.image='duck'+str(duck_num)
    if duck.left > WIDTH and duck.image != 'duck_hurt':
        duck.right = 0
    background.topright=background.topright[0]+1,0

def draw():
    global shells_remaining
    #screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.clear()
    background.draw()
    if shells_remaining>0:
        duck.draw()
    else:
        screen.draw.textbox("You killed "+str(kills)+" out of " +str(SHELLS)+
                            " ducks. Proud of yourself?",((20,20),(500,500)))
    print(screen.surface.get_at((100, 100)))
    
def on_mouse_down(pos):
    global shells_remaining
    shells_remaining-=1
    if duck.collidepoint(pos):
        set_duck_hurt()
    else:
        sounds.quack_ok.play()
def set_duck_hurt():
    global kills
    kills+=1
    duck.image = 'duck_hurt'
    sounds.quack.play()
    clock.schedule_unique(set_duck_normal, 1.0)

def set_duck_normal():
    global duck_speed
    duck_speed+=1
    duck.image = 'duck0'
    duck.topright = 0, randint(10,HEIGHT-300)
    
    