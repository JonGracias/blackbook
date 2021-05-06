# Imports
import os
import pickle
import sys
import pygame
import addict




def main():
    pygame.init()
    # load the sound files


    while True: # main game loop
        clickedButton = None # button that was clicked (set to buttonColor1, RED, GREEN, or BLUE)
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

        DISPLAYSURF.blit(infoSurf, infoRect)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = BUTTONCOLOR[0]
                elif event.key == K_w:
                    clickedButton = BUTTONCOLOR[1]
                elif event.key == K_a:
                    clickedButton = BUTTONCOLOR[2]
                elif event.key == K_s:
                    clickedButton = BUTTONCOLOR[3]
                elif event.key == K_e:
                    clickedButton = BUTTONCOLOR[4]
                elif event.key == K_d:
                    clickedButton = BUTTONCOLOR[5]



        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice(BUTTONCOLOR))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                # pushed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pushed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0 # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # pushed the incorrect button, or has timed out
                gameOverAnimation()
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def findRect(color):
    if color == BUTTONCOLOR[0]:
        return RECT1
    elif color == BUTTONCOLOR[1]:
        return RECT2
    elif color == BUTTONCOLOR[2]:
        return RECT3
    elif color == BUTTONCOLOR[3]:
        return RECT4
    elif color == BUTTONCOLOR[4]:
        return RECT5
    elif color == BUTTONCOLOR[5]:
        return RECT6

def flashButtonAnimation(color, animationSpeed=50):
    r = color[0]
    print(r)
    b = color[1]
    print(b)
    g = color[2]
    print(g)
   # i = 16
    newRgb = []
    for i in color:
       newRgb.append(color[i] + 16)

    print(newRgb)
    sound = BEEP1
    flashColor = (WHITE)
    print(flashColor)
    rectangle = findRect(color)
    

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            DISPLAYSURF.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))


def drawButtons():
    global BUTTONCOLOR
    

    for i in range (5):
        pygame.draw.rect(DISPLAYSURF, BUTTONCOLOR[0], RECTANGLES[i])
    
        
        


def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed): # animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0, 0))

        drawButtons() # redraw the buttons on top of the tint

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor


def gameOverAnimation(color=WHITE, animationSpeed=50):
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play() # play all four beeps at the same time, roughly.
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color
    for i in range(3): # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step): # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def getButtonClicked(x, y):
    if RECT1.collidepoint( (x, y) ):
        return BUTTONCOLOR[0]
    elif RECT2.collidepoint( (x, y) ):
        return BUTTONCOLOR[1]
    elif RECT3.collidepoint( (x, y) ):
        return BUTTONCOLOR[2]
    elif RECT4.collidepoint( (x, y) ):
        return BUTTONCOLOR[3]
    elif RECT5.collidepoint( (x, y) ):
        return BUTTONCOLOR[4]
    elif RECT6.collidepoint( (x, y) ):
        return BUTTONCOLOR[5]
    return None


if __name__ == '__main__':
    main()