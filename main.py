import RPi.GPIO as GPIO;
from time import sleep
from os import path, listdir
from random import choice
import sound

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def callback(channel):
	print "Press detected! Doorbell..."
	music_files = listdir('./sounds')
	music_file = choice(filter(lambda x: x != ".gitignore", music_files))
	sound.play_sound(path.realpath(path.join("./sounds", music_file)))

GPIO.add_event_detect(11, GPIO.RISING, callback=callback, bouncetime=1500)

while True:
	pass
