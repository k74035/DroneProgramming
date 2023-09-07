import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def getKeyboardInput():
    lr, fb, ud, yv, command = 0, 0, 0, 0, None
    speed = 50

    if getKey("LEFT"): lr = -speed
    elif getKey("RIGHT"): lr = speed

    if getKey("UP"): fb = speed
    elif getKey("DOWN"): fb = -speed

    if getKey("w"): ud = speed
    elif getKey("s"): ud = -speed

    if getKey("a"): yv = speed
    elif getKey("d"): yv = -speed

    if getKey("q"): command = 'land'
    if getKey("e"): command = 'takeoff'
    if getKey("n"): command = 'flip_left'
    if getKey("m"): command = 'flip_right'

    return [lr, fb, ud, yv, command]

'''
    vals = getKeyboardInput()
    if vals[4] is not None:
        if vals[4] == 'land':
            me.land()
        elif vals[4] == 'takeoff':
            me.takeoff()
        elif vals[4] == 'flip_left':
            me.flip_left()
        elif vals[4] == 'flip_right':
            me.flip_right()
    else:
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
'''