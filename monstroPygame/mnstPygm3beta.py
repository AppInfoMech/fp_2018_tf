import pygame
pygame.init()


#Sprites
charSprite = pygame.image.load('ufo.png')
bg = pygame.image.load('space1.png')
goldMet = pygame.image.load('meteor.png')
blkHole = pygame.image.load('blackhole2.png')
exitSprite = pygame.image.load('exit.png')

#Sounds
music = pygame.mixer.music.load('macintosh+.mp3') 
pygame.mixer.music.play(-1)
pickupSound = pygame.mixer.Sound('pickup.wav')
death = pygame.mixer.Sound('death.wav')
warp = pygame.mixer.Sound('warpSound.wav')
victory = pygame.mixer.Sound('victory.wav')

clock = pygame.time.Clock()

#Player Class
class player():
    def __init__(self, charX, charY, charWidth, charHeight):
        self.charX = charX
        self.charY = charY
        self.charWidth = charWidth
        self.charHeight = charHeight
        global hasGold
        self.charVel = 3
        self.hitbox = (self.charX + 20)

#Meteor Class
class meteor():
    def __init__(self, metX, metY, metWidth, metHeight):
        self.metX = metX
        self.metY = metY
        self.metWidth = metWidth
        self.metHeight = metHeight


#Black Hole Class
class bHole():
    def __init__(self, bHX, bHY, bHWidth, bHHeight, destination, vel):
        self.bHX = bHX
        self.bHY = bHY
        self.bHWidth = bHWidth
        self.bHHeight = bHHeight
        self.destination = destination
        self.vel = vel
        self.path = [self.bHX, self.destination]

#Collision Functions
def checkGCollision():
    global hasGold
    if hasGold == False:
        if ufo.charX > met.metX and ufo.charX < met.metX + met.metWidth or ufo.charX + ufo.charWidth > met.metX and ufo.charX + ufo.charWidth < met.metX + met.metWidth:
            if ufo.charY > met.metY and ufo.charY < met.metY + met.metWidth:
                pickupSound.play()
                hasGold = True
            elif ufo.charY + ufo.charWidth > met.metY and ufo.charY + ufo.charWidth < met.metY + met.metWidth:
                pickupSound.play()
                hasGold = True

def checkBHCollision():
    global dead
    global gameOn
    if dead == False:
        if ufo.charX > bH1.bHX and ufo.charX < bH1.bHX + bH1.bHWidth or ufo.charX + ufo.charWidth > bH1.bHX and ufo.charX + ufo.charWidth < bH1.bHX + bH1.bHWidth:
            if ufo.charY > bH1.bHY and ufo.charY < bH1.bHY + bH1.bHWidth:
                death.play()
                dead = True
                pygame.mixer.music.stop()
                pygame.time.delay(5000)
                gameOn = False
            elif ufo.charY + ufo.charWidth > bH1.bHY and ufo.charY + ufo.charWidth < bH1.bHY + bH1.bHWidth:
                death.play()
                dead = True
                pygame.mixer.music.stop()
                pygame.time.delay(5000)
                gameOn = False
        
        if ufo.charX > bH2.bHX and ufo.charX < bH2.bHX + bH2.bHWidth or ufo.charX + ufo.charWidth > bH2.bHX and ufo.charX + ufo.charWidth < bH2.bHX + bH2.bHWidth:
            if ufo.charY > bH2.bHY and ufo.charY < bH2.bHY + bH2.bHWidth:
                death.play()
                dead = True
                pygame.mixer.music.stop()
                pygame.time.delay(5000)
                gameOn = False
            elif ufo.charY + ufo.charWidth > bH2.bHY and ufo.charY + ufo.charWidth < bH2.bHY + bH2.bHWidth:
                death.play()
                dead = True
                pygame.mixer.music.stop()
                pygame.time.delay(5000)
                gameOn = False

        if ufo.charX > bH3.bHX and ufo.charX < bH3.bHX + bH3.bHWidth or ufo.charX + ufo.charWidth > bH3.bHX and ufo.charX + ufo.charWidth < bH3.bHX + bH3.bHWidth:
            if ufo.charY > bH3.bHY and ufo.charY < bH3.bHY + bH3.bHWidth:
                death.play()
                dead = True
                pygame.mixer.music.stop()
                pygame.time.delay(5000)
                gameOn = False
                
            elif ufo.charY + ufo.charWidth > bH3.bHY and ufo.charY + ufo.charWidth < bH3.bHY + bH3.bHWidth:
                death.play()
                dead = True
                pygame.mixer.music.stop()
                pygame.time.delay(5000)
                gameOn = False
                

def checkExitCollision():
    global hasGold
    global gameOn
    if hasGold == True:
        if ufo.charX > 470 and ufo.charX < 470 + 125 or ufo.charX + ufo.charWidth > 470 and ufo.charX + ufo.charWidth < 470 + 125:
            if ufo.charY > 470 and ufo.charY < 470 + 125:
                global gameOn
                pygame.mixer.music.stop()
                warp.play()
                pygame.time.delay(3000)
                victory.play()
                pygame.time.delay(2200)
                gameOn = False
            elif ufo.charY + ufo.charWidth > 470 and ufo.charY + ufo.charWidth < 470 + 125:
                pygame.mixer.music.stop()
                warp.play()
                pygame.time.delay(3000)
                victory.play()
                pygame.time.delay(2200)
                gameOn = False


#Palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (3, 214, 62)
RED = (255, 0, 0)

#Screen parameters
winWidth = 600
winHeight = 600

#Screen creation
screen = pygame.display.set_mode((winWidth, winHeight))

pygame.display.set_caption("Treasure Hunt: Space Trip")

print("\n\n\nWelcome to Treasure Hunt: Space Trip!\nUse the arrow keys to move your spaceship through space.\nGet the golden asteroid and bring it to the exit portal, but be careful!\nAvoid the black holes or you'll be stuck in space forever!\nGood Luck!")

#Main game conditions

hasGold = False
gameOn = True
dead = False

ufo = player(15, 540, 42, 42)
met = meteor(370, 75, 40, 40)
bH1 = bHole(35, 40, 120, 120, 450, 4)
bH2 = bHole(240, 210, 120, 120, 35, 2)
bH3 = bHole(35, 390, 120, 120, 450, 2)


#Game Loop
while gameOn == True:
    screen.blit(bg, (0,0))
    screen.blit(blkHole, (bH1.bHX, bH1.bHY, bH1.bHWidth, bH1.bHHeight))
    screen.blit(blkHole, (bH2.bHX, bH2.bHY, bH2.bHWidth, bH2.bHHeight))
    screen.blit(blkHole, (bH3.bHX, bH3.bHY, bH3.bHWidth, bH3.bHHeight))
    screen.blit(charSprite, (ufo.charX, ufo.charY, ufo.charWidth, ufo.charHeight))
    if hasGold == False:
        screen.blit(goldMet, (met.metX, met.metY))
    else:
        screen.blit(goldMet, (ufo.charX, ufo.charY))
        screen.blit(exitSprite, (470, 470))
    pygame.display.update()
    clock.tick(60)
    screen.fill(BLACK)

    #if (ufo.charX, ufo.charY) == (met.metX, met.metY):
        #hasGold = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    #Player Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ufo.charX > ufo.charVel:
        ufo.charX -= ufo.charVel
    if keys[pygame.K_RIGHT] and ufo.charX < winWidth - ufo.charWidth - ufo.charVel:
        ufo.charX += ufo.charVel
    if keys[pygame.K_UP] and ufo.charY > ufo.charVel:
        ufo.charY -= ufo.charVel
    if keys[pygame.K_DOWN] and ufo.charY < winHeight - ufo.charHeight - ufo.charVel:
        ufo.charY += ufo.charVel

    #Obstacle Movement
    if bH1.vel > 0:
        if bH1.bHX + bH1.vel < bH1.path[1]:
            bH1.bHX += bH1.vel
        else:
            bH1.vel = bH1.vel * -1
    else:
        if bH1.bHX - bH1.vel > bH1.path[0]:
            bH1.bHX += bH1.vel
        else:
            bH1.vel = bH1.vel * -1
    
    if bH2.vel > 0:
        if bH2.bHX + bH2.vel < bH2.path[1]:
            bH2.bHX += bH2.vel
        else:
            bH2.vel = bH2.vel * -1
    else:
        if bH2.bHX - bH2.vel > bH2.path[0]:
            bH2.bHX += bH2.vel
        else:
            bH2.vel = bH2.vel * -1

    if bH3.vel > 0:
        if bH3.bHX + bH3.vel < bH3.path[1]:
            bH3.bHX += bH3.vel
        else:
            bH3.vel = bH3.vel * -1
    else:
        if bH3.bHX - bH3.vel > bH3.path[0]:
            bH3.bHX += bH3.vel
        else:
            bH3.vel = bH3.vel * -1


    #Black holes collision
    checkBHCollision()
    
    #Gold collision
    checkGCollision() 

    #Exit collision
    checkExitCollision()


pygame.quit()
