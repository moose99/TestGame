# holds the code for asteroids
# __author__ = 'zac_000'

import math

ASTEROID_SPEED = 5

# initialize variables to hold the space rectangle and image
asteroidRect = None
asteroidImage = None
asteroidDirX = 1
asteroidDirY = 1


# func to create the space
def SetupAsteroid(game):
    # use 'global' to indicate that we are changing the spaceRect/spaceImage vars declared outside the function
    global asteroidRect
    global asteroidImage
    ASTEROID_WIDTH = 1
    ASTEROID_HEIGHT = 1
    rotation = 0
    dirX = math.cos(math.radians(rotation))
    dirY = -math.sin(math.radians(rotation))

    asteroidRect = game.Rect(0, 0, ASTEROID_WIDTH, ASTEROID_HEIGHT)
    asteroidImage = game.image.load('assets/rock.gif')

def DrawAsteroid(surface):
    surface.blit(asteroidImage, asteroidRect)

def Amove(surface):
    global asteroidDirX, asteroidDirY, ASTEROID_SPEED, asteroidRect

    # move the bullet in the right direction
    asteroidRect.centerx += asteroidDirX * ASTEROID_SPEED
    asteroidRect.centery += asteroidDirY * ASTEROID_SPEED

    # check for bullet going off screen

    if (asteroidRect.centerx > surface.get_width()):
        asteroidRect.centerx -= surface.get_width()

    if (asteroidRect.centerx < 0):
        asteroidRect.centerx+= surface.get_width()

    if (asteroidRect.centery > surface.get_height()):
        asteroidRect.centery -= surface.get_height()

    if (asteroidRect.centery < 0):
        asteroidRect.centery += surface.get_height()


