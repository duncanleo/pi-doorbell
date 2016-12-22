import os

def get_sound_file():
    with open(os.path.realpath("./sound.txt")) as f:
		return f.readlines()[0].replace("\r\n", "").replace("\n", "")
