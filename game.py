# Step 1: Hello Bunny
# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("resources/images/dude.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (100,100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)



# Step 2: Add Scenery

# Step 3: Make the Bunny Move

# Step 4: Turning the Bunny

# Step 5: Shoot, Bunny, Shoot!

# Step 6: Take Up Arms! Badgers!

# Step 7: Collisions with Badgers and Arrows

# Step 8: Add a HUD with Health Meter and Clock

# Step 9: Win or Lose

# Step 10: Gratuitous Music and Sound Effects!
