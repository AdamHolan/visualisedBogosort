import pygame
import random

# some colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()

# screen dimensions
width = 700
height = 600

size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Bogo Test')

# loop until close
done = False

# screen updates (for readability)
clock = pygame.time.Clock()

# Establishing globals
numElements = 5
sortedList = list(range(1, numElements + 1))
newList = list(range(1, numElements + 1))
random.shuffle(newList)

# Generate random colour. Looks pretty and saves time hardcoding stuff idk
def randColour():
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return colour

# Set up a list of random colours. ColourList = [randColour]*5 only calls randColour() once, hence this implementation
colourList = []
for i in range(numElements):
    colourList.append(randColour())

# One bogosort instruction
def bogo():
    if newList != sortedList:
        random.shuffle(newList)


# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Wipes screen every time to avoid clipping and stuff
    screen.fill(black)

    # Draw Lines based upon it's location in the newList, as well as it's value to determine height. Designed to
    # avoid any kind of hard coding and work with numbers > 5 (not that you should ever try to)
    # Colour could in theory be personalised had I made each rectangle an object.
    for i in range(len(newList)):
        pygame.draw.rect(screen, width, [(width/numElements) * i, 0, width/numElements, (height/numElements)*newList[i]])

    # Execute a round of bogo
    bogo()

    # Display graphics
    pygame.display.flip()


    clock.tick(60)
