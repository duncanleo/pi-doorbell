import RPi.GPIO as GPIO;
from time import sleep
from os import path
import storage, sound

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Starting the wait"
while True:
	if (GPIO.input(11) == False):
		print "Press detected! Doorbell..."
		sound.play_sound(path.realpath(path.join("./sounds", storage.get_sound_file())))
	sleep(0.2)
