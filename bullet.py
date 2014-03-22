# holds the code for bullets, bullets are kept in a list
__author__ = 'Mus'

# need math library functions
import math

# bullet constant values
BULLET_SPEED = 8

# initialize variables to hold the bullet rectangle and image
bulletImage = None
bulletRect = []
bulletDirX = []
bulletDirY = []
bulletSound = None

# bullet initialization
def SetupBullet(game):
    global bulletImage, bulletSound
    bulletImage = game.image.load('assets/circle.png')
    bulletSound = game.mixer.Sound('assets/tx0_fire1.wav')

# func to create the bullet
def FireBullet(game, x, y, rotation):
    # use 'global' to indicate that we are changing the bulletRect/bulletImage vars declared outside the function
    global bulletRect, bulletImage
    BULLET_WIDTH = 8
    BULLET_HEIGHT = 8
    dirX = math.cos(math.radians(rotation))
    dirY = -math.sin(math.radians(rotation))
    x += dirX
    y += dirY
    rect = game.Rect(x-(BULLET_WIDTH/2), y-(BULLET_HEIGHT/2), BULLET_WIDTH, BULLET_HEIGHT)
    bulletRect.insert(0, rect)
    bulletDirX.insert(0, dirX)
    bulletDirY.insert(0, dirY)    # flip Y
    bulletSound.play()

# remove a bullet fromthe list
def RemoveBullet(i):
    del bulletRect[i]
    del bulletDirX[i]
    del bulletDirY[i]

# move all bullets
def MoveBullets(surface):
    global bulletRect
    # loop through the list of bullets, starting at the end
    i = len(bulletRect)-1
    while (i>=0):
        # move the bullet in the right direction
        bulletRect[i].centerx += bulletDirX[i] * BULLET_SPEED
        bulletRect[i].centery += bulletDirY[i] * BULLET_SPEED
        # check for bullet going off screen
        if (bulletRect[i].centerx > surface.get_width() or bulletRect[i].centery > surface.get_height() or
            bulletRect[i].centerx < 0 or bulletRect[i].centery < 0):
            RemoveBullet(i)
        i -= 1

# draw bullets on the screen
def DrawBullet(surface):
    MoveBullets(surface)
    # now draw all bullets
    for rect in bulletRect:
        surface.blit(bulletImage, rect)
