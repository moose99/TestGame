__author__ = 'Zac'

asteroidRect = None
asteroidImage = None

def SetupAsteroid(game):

    global asteroidRect
    global asteroidImage
    asteroidImage = game.image.load('assets/739px-Asteroid-XWA')


def DrawAsteroid(surface):
    surface.blit(asteroidImage, asteroidRect)