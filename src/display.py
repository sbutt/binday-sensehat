# src/display.py

from sense_hat import SenseHat
import time

sense = SenseHat()
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

# =====================================================
# NEW: Better environment display (no scrolling)
# =====================================================

def show_environment():
    """Fully static display: Humidity (left) + Pressure (right)"""
    try:
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()

        sense.clear()

        # Humidity bar - LEFT column
        hum_height = max(0, min(8, int(humidity / 13)))
        for y in range(8):
            if y < hum_height:
                colour = (0, 160, 255) if humidity < 70 else (0, 255, 200)
                sense.set_pixel(0, 7 - y, colour)
            else:
                sense.set_pixel(0, 7 - y, (8, 8, 12))

        # Pressure bar - RIGHT column
        press_height = max(0, min(8, int((pressure - 970) / 9)))
        for y in range(8):
            if y < press_height:
                colour = (255, 200, 60) if pressure >= 1010 else (120, 180, 255)
                sense.set_pixel(7, 7 - y, colour)
            else:
                sense.set_pixel(7, 7 - y, (8, 8, 12))

        # Tiny static labels
        sense.set_pixel(1, 0, (100, 100, 100))  # H
        sense.set_pixel(6, 0, (180, 180, 80))   # P

    except Exception:
        sense.clear((40, 0, 0))  # Red screen if something goes wrong
