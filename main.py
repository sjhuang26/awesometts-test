import pyautogui as g
import time as t
import keyboard as k
from random import randint

g.FAILSAFE = True

size = g.size()

while True:
    x, y = g.position()
    #g.dragTo(randint(0, size[0]), randint(0, size[1]), 1, g.easeInElastic)
    #g.click()
    if k.is_pressed('k'):
        g.hotkey('ctrl', 'a')