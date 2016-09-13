package sound

import (
	"os"
	"os/exec"
)

// PlaySound ...
func PlaySound(path string) {
	cmd := exec.Command("omxplayer", "-o", "local", path)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stdout
	cmd.Run()
}
