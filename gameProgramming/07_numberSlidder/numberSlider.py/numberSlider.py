# NUmber Slider, Ceon based on project by AI Sweigart, v0.0
import sys, random, pygame
# sys module provides access to system resoureces 

from pygame.locals import*
#Allows us to call function from pygame using just the function name instead of module.function()
#Example: We can draw() instead of pygame.draw()
#Constatants are in all caps so it doesnt change

#Constants for Game Board
BOARDWIDTH= 4 # COLUMS
BOARDHEIGHT= 4 #ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 #MEASURED IN PIXLES
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 # THIS IS A MAXIMUM VALUE CANT MAKE SLOW COMPUTER RUN FASTER
BLANK = None 

# COLOR VALUES IN (R, G, B) FORMAT
# 0 = NO VALUE, 255 = MAX VALUE
BLACK = (0,0,0)
WHITE =(255,255,255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

#BOARD SETUP
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE= 20 #PIXELS

# BUTTON SETUP
BUTTONCOLOR= WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGE = WHITE

# ESTABLISH WINDOW MARGINS
XMARGINS = int((WINDOWWIDTH - (TILESIZE*BOARDWIDTH + (BOARDWIDTH - 1 /2))))
# XMARGINS = int((WINDOWWIDTH - (TILESIZE*BOARDWIDTH + (3)))) /2
# XMARGINS = int((WINDOWWIDTH - (320 + (3))))) /2
# XMARGINS = int((WINDOWWIDTH - (323)))) /2
# XMARGINS = int((640 - 161.5))
# XMARGINS = int((WINDOWWIDTH - (TILESIZE*BOARDWIDTH + (BOARDWIDTH - 1)))) /2
# XMARGINS = int(478.5)))) 
# XMARGIN = 480
print(XMARGINS)
YMARGIN = int((WINDOWWIDTH - (TILESIZE*BOARDWIDTH + (BOARDWIDTH - 1 /2))))

# DIRECTIONS
UP='up'
DOWN = 'down'
LEFT= 'left'
RIGHT = 'right'