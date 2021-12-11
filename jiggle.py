#/usr/bin/env python3

from pyautogui import moveTo
from random import randint
from time import sleep, localtime, strftime

if __name__ == "__main__":
	interval = 5 * 60
	print("jiggling every {} seconds".format(interval))
	print("Hit <ctrl> - <c> to stop")
	while True:
		x = randint(100, 1000)
		y = randint(100, 800)
		moveTo(x, y, duration=0.25)
		moveTo(y, x, duration=0.3)
		moveTo((x+100)/2, (y+100)/2, duration=0.5)
		print("jiggled at {}".format(strftime("%a %d %b %Y %H:%M:%S", localtime())), end = "\r")
		sleep(interval)
