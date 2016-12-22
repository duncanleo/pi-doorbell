import RPi.GPIO as GPIO;
from time import sleep
import subprocess, threading
import storage, sound

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Starting the wait"
while True:
	if (GPIO.input(11) == False):
		print "Press detected! Doorbell..."
		sound.play_sound(storage.get_sound_file())
	sleep(0.2)
