package storage

import (
	"io/ioutil"
	"strings"
)

// GetSoundFile ...
func GetSoundFile() (string, error) {
	dat, err := ioutil.ReadFile("sound.txt")
	if err != nil {
		return "", err
	}
	cleaned := strings.Replace(string(dat), "\n", "", -1)
	return cleaned, nil
}
