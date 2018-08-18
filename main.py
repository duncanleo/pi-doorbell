import RPi.GPIO as GPIO
from time import sleep
from os import path, listdir, environ
from random import choice
import sound
import urllib2
import urllib

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

post_data = urllib.urlencode({
	'ding': 'dong',
	'dong': 'ding'
})

print "Starting the wait"
while True:
	if (GPIO.input(11) == False):
		print "Press detected! Doorbell..."
		if environ['REQUEST_URL']:
			req = urllib2.Request(environ['REQUEST_URL'], post_data)
			urllib2.urlopen(req).read()
		music_files = listdir('./sounds') 
		music_file = choice(filter(lambda x: x != ".gitignore", music_files)) 
		sound.play_sound(path.realpath(path.join("./sounds", music_file)))	
	sleep(0.2)
