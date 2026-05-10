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
    """Static display: Temperature bar graph + values"""
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    sense.clear()

    temp_c = int(temp)

    # === Temperature Bar (Left column - tall and clear) ===
    # Scale roughly 0°C to 40°C
    bar_height = max(0, min(8, int((temp_c + 5) / 5.5)))

    for y in range(8):
        if y < bar_height:
            # Temperature color gradient
            if temp_c < 12:
                colour = (0, 100, 255)      # cold blue
            elif temp_c < 18:
                colour = (0, 255, 200)      # cyan
            elif temp_c < 24:
                colour = (100, 255, 50)     # green
            else:
                colour = (255, 100, 0)      # warm orange
            sense.set_pixel(0, 7 - y, colour)
        else:
            sense.set_pixel(0, 7 - y, (10, 10, 10))  # faint background

    # === Small indicators on the right ===
    # Humidity (top right - 3 pixels)
    hum_level = min(3, int(humidity / 35))
    for x in range(1, 4):
        colour = (80, 180, 255) if x-1 < hum_level else (25, 25, 25)
        sense.set_pixel(x, 0, colour)

    # Pressure (middle right - 3 pixels)
    press_level = min(3, int((pressure - 990) / 12))
    for x in range(1, 4):
        colour = (255, 220, 80) if x-1 < press_level else (25, 25, 25)
        sense.set_pixel(x, 3, colour)

    # === Show temperature number briefly (without clearing bar) ===
    # We show it once then the bar stays
    sense.show_message(f"{temp_c}C", scroll_speed=0.09, text_colour=(180, 180, 180))

    # Optional: redraw the bar after message (in case it cleared)
    time.sleep(0.3)
    # Redraw bar quickly
    for y in range(8):
        if y < bar_height:
            sense.set_pixel(0, 7 - y, colour)
        else:
            sense.set_pixel(0, 7 - y, (10, 10, 10))
