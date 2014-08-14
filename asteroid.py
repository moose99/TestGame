__author__ = 'zac_000'

# initialize variables to hold the space rectangle and image
asteroidRect = None
asteroidImage = None

# func to create the space
def SetupAsteroid(game):
    # use 'global' to indicate that we are changing the spaceRect/spaceImage vars declared outside the function
    global asteroidRect
    global asteroidImage
    ASTEROID_WIDTH = 1
    ASTEROID_HEIGHT = 1
    asteroidRect = game.Rect(0, 0, ASTEROID_WIDTH, ASTEROID_HEIGHT)
    asteroidImage = game.image.load('assets/asteroidrock.png')

def DrawAsteroid(surface):
    surface.blit(asteroidImage, asteroidRect)