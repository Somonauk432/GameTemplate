import pygame

gameSpeed = 20

#Colors
white = (255, 255, 255)
red   = (255,   0,   0)
blue  = (  0,   0, 255)
green = (  0, 255,   0)
    
class Game(object):
    """Class Level Variables"""

    #Clock
    clock = pygame.time.Clock()
    
    #Screen Setup
    screen_width = 400
    screen_height = 400

    #Grid Setup
    noTilesX = 8
    noTilesY = 8
    tile_width = screen_width / noTilesX
    tile_height = screen_height / noTilesY

    #Initialization
    def __init__(self):
        """Place initialization methods here"""
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height], 0, 32)
        self.screen.fill(white)
    
    #Load Content
    def loadContent(self):
        "Place content loading here"
        #print "content loaded"

    #Update Calls
    def update(self):
        "Update calls here"
        #print "updating..."
        self.clock.tick(gameSpeed)
    
    #Draw Calls
    def draw(self):
        "Draw calls here"
        #print "drawing"