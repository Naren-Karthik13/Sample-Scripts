from pynput.mouse import Controller
from random import randint
from time import sleep

mouse = Controller()
while True:
    mouse.move(randint(-10, 10), randint(-10, 10))
    sleep(1)