from pynput import keyboard
import pydirectinput
import pyautogui
import time

active = False
state = 0

def on_press(key):
	global active
	print (key)
	if key == keyboard.Key.page_down:
		if state == 1:
			pydirectinput.keyUp('w')
		if state == 2:
			pydirectinput.mouseUp()
		if state == 3:
			autoScrap()
		active = False
	if key == keyboard.Key.page_up:
		print ('starting')
		active = True
		while active:
			if state == 1:
				autoWalk()
			if state == 2:
				autoBuild()
			if state == 3:
				autoScrap()

def autoWalk():
	pydirectinput.keyDown('w')

def autoBuild():
	pydirectinput.mouseDown()

def autoScrap():
	pydirectinput.mouseDown()
	time.sleep(2)
	pydirectinput.mouseUp()
	time.sleep(2)

def menu():
	global state
	global active
	print('Choose option\n    [+]1.Drive or Walk\n    [+]2.Build\n    [+]3.Scrap\nPress Page Up to start')
	state = int(input())
	active = True

menu()
with keyboard.Listener(on_press=on_press) as listener:
	while active == True:
		print ('script running')
		time.sleep(5)
	listener.join()