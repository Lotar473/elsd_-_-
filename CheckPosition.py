import pyautogui as pag
import keyboard
import schedule
import time
import datetime
from PIL import ImageGrab

while True:
    if keyboard.is_pressed("F10"):
        t1 = pag.position()
        print(t1)
        screen = ImageGrab.grab()
        rgb = screen.getpixel(t1)
        print(rgb)
        time.sleep(0.5)
        break
while True:
    if keyboard.is_pressed("F10"):
        t2 = pag.position()
        print(t2)
        screen = ImageGrab.grab()
        rgb = screen.getpixel(t2)
        print(rgb)
        time.sleep(0.5)
        break