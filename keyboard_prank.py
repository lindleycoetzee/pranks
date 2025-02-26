import pyautogui
import time

while True:
	time.sleep(0.5)
	pyautogui.press('win')
	time.sleep(0.5)
	pyautogui.write('notepad', interval=0.25)
	time.sleep(0.5)
	pyautogui.press('enter')
	time.sleep(0.75)
	pyautogui.press('capslock')
	pyautogui.write('I AM WATCHING YOU', interval=0.25)
	time.sleep(3)
	pyautogui.press('win')
	time.sleep(2.5)
	pyautogui.write('notepad', interval=0.25)
	time.sleep(0.5)
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.write('I WILL NOT STOP', interval=0.25)
	time.sleep(2.5)
	# to stop use fail safe
