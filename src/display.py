# src/display.py

from sense_hat import SenseHat
import time

sense = SenseHat()

# much dimmer
sense.low_light = True

# =====================================================

COLOURS = {
    "Refuse Collection (General Rubbish)": (25, 25, 25),
    "Recycling Collection": (0, 80, 0),
    "Garden Waste Collection (Brown Bin)": (80, 40, 0),
    "Food Waste Collection": (80, 80, 0),
}

# =====================================================

def show(colour):
    sense.clear(colour)

# =====================================================

def flash(colour):

    for _ in range(4):

        sense.clear(colour)

        time.sleep(0.4)

        sense.clear()

        time.sleep(0.4)

# =====================================================

def clear():
    sense.clear()
