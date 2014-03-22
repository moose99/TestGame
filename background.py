# contains code for the space (background) object
__author__ = 'Mus'

# initialize variables to hold the space rectangle and image
bgndRect = None
bgndImage = None

# func to create the space
def SetupBgnd(game):
    # use 'global' to indicate that we are changing the spaceRect/spaceImage vars declared outside the function
    global bgndRect
    global bgndImage
    BGND_WIDTH = 1280
    BGND_HEIGHT = 796
    bgndRect = game.Rect(0, 0, BGND_WIDTH, BGND_HEIGHT)
    bgndImage = game.image.load('assets/B1_stars.png')

def DrawBgnd(surface):
    surface.blit(bgndImage, bgndRect)