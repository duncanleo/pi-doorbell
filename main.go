package main

import (
	"fmt"
	"log"
	"sound"
	"storage"
	"time"

	"github.com/stianeikeland/go-rpio"
)

func main() {
	err := rpio.Open()
	if err != nil {
		log.Println(err)
		return
	}

	log.Println("Connecting GPIO...")

	pin := rpio.Pin(17) // 17 == 11 as this lib uses BCM board mode
	pin.Mode(rpio.Input)
	pin.PullUp()

	t := time.NewTicker(300 * time.Millisecond)

	log.Println("Waiting for presses!")

	for {
		if pin.Read() == rpio.Low {
			// Pressed
			log.Println("Pressed!")
			soundFile, err := storage.GetSoundFile()
			if err != nil {
				log.Println(err)
				continue
			}
			absPath := fmt.Sprintf("/home/pi/doorbell/sounds/%s", soundFile)
			sound.PlaySound(absPath)
		}
		<-t.C
	}
}
