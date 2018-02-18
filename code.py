import os
import random

from digitalio import DigitalInOut, Direction, Pull
import audioio
import board
import touchio

# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

# Get all files in the toots directory
toots = os.listdir("toots")

# Enable the pad
cushion = touchio.TouchIn(board.A2)

def toot():
    # Open a random toot for playing
    # NOTE: no `os.path` module
    f = open("toots/{}".format(random.choice(toots)), "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
    # Block until finished
    while a.playing:
        pass


while True:
    if cushion.value:
        print("Gotcha! {}".format(cushion.raw_value))
        toot()
