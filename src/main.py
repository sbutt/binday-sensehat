# src/main.py

from datetime import datetime, date
import time
import json
import os

from rules import tomorrow_bins
from display import show, flash, clear, COLOURS, show_environment
from logger import setup_logger

from sense_hat import SenseHat

# =====================================================

STATE_FILE = "data/state.json"

sense = SenseHat()

logger = setup_logger()

# =====================================================

def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "acknowledged_date": None
        }

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)

    except Exception:
        return {
            "acknowledged_date": None
        }

# =====================================================

def save_state(state):
    os.makedirs("data", exist_ok=True)

    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

# =====================================================

def acknowledged_today(state):
    return state.get("acknowledged_date") == str(date.today())

# =====================================================

def acknowledge(state):
    state["acknowledged_date"] = str(date.today())
    save_state(state)

# =====================================================

def main():

    logger.info("Binday system started")

    state = load_state()

    while True:

        now = datetime.now()

        # ============================================
        # joystick acknowledge
        # ============================================

        for event in sense.stick.get_events():

            if event.action == "pressed":

                acknowledge(state)

                clear()

                logger.info("Reminder acknowledged")

        # ============================================
        # already acknowledged today?
        # ============================================

        if acknowledged_today(state):

            clear()

            time.sleep(5)

            continue

        # ============================================
        # determine tomorrow bins
        # ============================================

        bins = tomorrow_bins()

        if not bins:
            # No bin collection tomorrow → show temperature / pressure / humidity
            show_environment()
            time.sleep(30)          # refresh every 30 seconds
            continue

        # ============================================
        # first bin colour
        # ============================================

        bin_name = bins[0]

        colour = COLOURS.get(bin_name, (20, 20, 20))

        # ============================================
        # before 7pm = solid
        # after 7pm = flashing
        # ============================================

        if now.hour < 19:

            show(colour)

            time.sleep(5)

        else:

            flash(colour)

        time.sleep(1)

# =====================================================

if __name__ == "__main__":
    main()
