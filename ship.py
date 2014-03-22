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
SHIP_SPEED_AMOUNT = .1
SHIP_DRAG_AMOUNT = 0.01
SHIP_MAX_SPEED = 6

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

# change ship rotation
def RotateShipCW():
    global shipRotation
    shipRotation -= SHIP_ROTATION_AMOUNT
    # handle wrapping of rotation value
    if (shipRotation < 0):
        shipRotation = 360 + shipRotation

# change ship's velocity
def MoveShip(thruster):
    global shipVelX, shipVelY

     # change velocity
    if (thruster):
        # find the current direction vector
        shipDirX = math.cos(math.radians(shipRotation))
        shipDirY = -math.sin(math.radians(shipRotation))    # flip Y

        # increase velocity using current direction
        shipVelX += shipDirX * SHIP_SPEED_AMOUNT
        shipVelY += shipDirY * SHIP_SPEED_AMOUNT

        # clamp velocity
        length = math.sqrt(shipVelX*shipVelX + shipVelY*shipVelY)  # hypotenuse
        if (length > SHIP_MAX_SPEED):
            shipVelX = shipVelX * SHIP_MAX_SPEED / length
            shipVelY = shipVelY * SHIP_MAX_SPEED / length
    else:
        # decrease velocity without changing direction
        length = math.sqrt(shipVelX*shipVelX + shipVelY*shipVelY)  # hypotenuse
        if (length >= SHIP_DRAG_AMOUNT ):
            shipVelX = shipVelX * (length-SHIP_DRAG_AMOUNT) / length
            shipVelY = shipVelY * (length-SHIP_DRAG_AMOUNT) / length
        else:
            shipVelX = 0
            shipVelY = 0

def TransformShip(surface, turnCCW, turnCW, thruster):
    # we'll be changing these globals
    global shipVelX, shipVelY, shipPosX, shipPosY
    # handle rotation
    if (turnCCW):
        RotateShipCCW()
    elif turnCW:
        RotateShipCW()

    # handle translation
    MoveShip(thruster)

    # update position based on current velocity and speed
    shipPosX += shipVelX
    shipPosY += shipVelY

    # wrap position
    if (shipPosX >= surface.get_width()):
        shipPosX -= surface.get_width()
    if (shipPosY >= surface.get_height()):
        shipPosY -= surface.get_height()

    if (shipPosX < 0):
        shipPosX = surface.get_width() + shipPosX
    if (shipPosY < 0):
        shipPosY = surface.get_height() + shipPosY
