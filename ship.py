# contains code for the ship object
__author__ = 'Mus'

# need math library functions
import math

# initialize variables to hold the ships rectangle and image and sounds
shipRect = None
shipImage = None
engineSound = None

# ship constant vars: size, rotation amount
SHIP_WIDTH = 30
SHIP_HEIGHT = 30
SHIP_ROTATION_AMOUNT = 4
SHIP_SPEED_AMOUNT = 1

# init vars to hold velocity, speed, position and rotation...
shipRotation = 0    # goes from 0 to 360
shipPosX = 250
shipPosY = 250
shipVelX = 0
shipVelY = 0


# func to create the ship
def SetupShip(game):
    # use 'global' to indicate that we are changing the shipRect/shipImage vars declared outside the function
    global shipRect
    global shipImage
    global engineSound
    shipRect = game.Rect(shipPosX-(SHIP_WIDTH/2), shipPosY-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)
    shipImage = game.image.load('assets/rocketship.png')
    engineSound = game.mixer.Sound('assets/engine_2.wav')

# draws the ship on the surface provided
def DrawShip(surface, game):
    # first apply ship rotation
    rotatedShipImage = game.transform.rotate(shipImage, shipRotation)
    rotatedRect = rotatedShipImage.get_rect()
    rotatedRect.center = shipRect.center    # use original image center, so always rotates around the same center

    # now apply ship translation
    rotatedRect.center = (shipPosX, shipPosY)

    # now draw it on screen
    surface.blit(rotatedShipImage, rotatedRect)

# change ship rotation
def RotateShipCCW():
    global shipRotation
    shipRotation += SHIP_ROTATION_AMOUNT
    # handle wrapping of rotation value
    if (shipRotation > 360):
        shipRotation = 360 - shipRotation

# change ship's velocity
def MoveShip(surface, thruster):
    global shipVelX, shipVelY, shipPosX, shipPosY

     # change velocity
    if (thruster):
        # find the current direction vector, using unit circle
        shipDirX = math.cos(math.radians(shipRotation))
        shipDirY = -math.sin(math.radians(shipRotation))    # flip Y

        # increase velocity using current direction
        shipVelX = shipDirX * SHIP_SPEED_AMOUNT
        shipVelY = shipDirY * SHIP_SPEED_AMOUNT

    else:
        shipVelX = 0
        shipVelY = 0

   # update position based on current velocity
    shipPosX += shipVelX
    shipPosY += shipVelY

    # wrap position if off screen
    if (shipPosX >= surface.get_width()):
        shipPosX -= surface.get_width()

# handles moving and turning the ship
def TransformShip(surface, turnCCW, turnCW, thruster):
    # handle rotation
    if (turnCCW):
        RotateShipCCW()

    # handle translation
    MoveShip(surface, thruster)


