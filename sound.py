import os, subprocess

def play_sound(path):
    play_process = subprocess.Popen(['omxplayer', '-o', 'local', os.path.realpath(path)], stdin=subprocess.PIPE, close_fds=True)
    # Wait for process to end
    play_process.wait()
