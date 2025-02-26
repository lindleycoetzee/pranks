import pyautogui
import time
import random

while True:
	x = random.randint(1,1920)
	y = random.randint(1,1080)
	time.sleep(0.5)
	pyautogui.moveTo(x, y, 1.5)
	# ctrl + F2 or us fail safe
