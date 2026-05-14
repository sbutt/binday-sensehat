# Binday Sense HAT

A Raspberry Pi Sense HAT system that displays bin collection status using:
- Rule-based schedule
- UK bank holiday adjustments
- Offline operation (no APIs or scraping)

## Features
- Green/brown/blue/grey bin mapping
- Bank holiday shift logic (+1 day)
- Flashing reminder after 7pm
- Joystick to acknowledge
- Fully offline

## Install

```bash
chmod +x install.sh
./install.sh
```

TODO:
- Make the black bin show as a white square with black in the middle.
- Update for June schedule.
- Get bank holidays from holidays python module instead of hard coding.
