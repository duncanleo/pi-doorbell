import RPi.GPIO as GPIO;
from time import sleep
from os import path, listdir
from random import choice
import sound

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Starting the wait"
while True:
	if (GPIO.input(11) == False):
		print "Press detected! Doorbell..."
		music_files = listdir('./sounds') 
		music_file = choice(filter(lambda x: x != ".gitignore", music_files)) 
		sound.play_sound(path.realpath(path.join("./sounds", music_file))) 
	sleep(0.2)
