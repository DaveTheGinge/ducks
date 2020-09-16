from random import randint
import pgzero
import pgzrun

duck = Actor('duck0')
duck.topright = 0, 10
background = Actor('pasture')
SHELLS = 20
shells_remaining = SHELLS
kills = 0
WIDTH = 1200
HEIGHT = 700

duck_speed = 1
background.topright = WIDTH, 0


def update():
    global duck_speed

    duck.left += duck_speed
    if(duck.image != 'duck_hurt'):
        duck_num = int(duck.image[-1])
        duck_num = (duck_num+1) % 6
        duck.image = 'duck'+str(duck_num)
    if duck.left > WIDTH and duck.image != 'duck_hurt':
        duck.right = 0
    background.topright = background.topright[0]+1, 0


def draw():
    global shells_remaining
    #screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.clear()
    background.draw()
    if shells_remaining > 0:
        duck.draw()
    else:
        if kills == 0:
            spiel = " ducks. Are you a vegitarian?."
        elif kills < SHELLS / 2:
            spiel = " ducks: Quackers."
        elif kills < SHELLS - 1:
            spiel = " ducks. Quacking."
        else:
            spiel = " ducks. Proud of yourself?"
        screen.draw.textbox("You got "+str(kills)+" out of " + str(SHELLS) +
                            spiel, ((20, 20), (500, 500)))
    #print(screen.surface.get_at((100, 100)))


def on_mouse_down(pos):
    global shells_remaining
    shells_remaining -= 1
    if duck.collidepoint(pos):
        set_duck_hurt()
    else:
        sounds.quack_ok.play()


def set_duck_hurt():
    global kills
    kills += 1
    duck.image = 'duck_hurt'
    sounds.quack.play()
    clock.schedule_unique(set_duck_normal, 1.0)


def set_duck_normal():
    global duck_speed
    duck_speed += 1
    duck.image = 'duck0'
    duck.topright = 0, randint(10, HEIGHT-300)

pgzrun.go()
