import pyautogui
import time

while True:
	x = 500
	y = 800
	time.sleep(0.5)
	pyautogui.moveTo(x, y, 1.5)

	# to stop use fail safe
