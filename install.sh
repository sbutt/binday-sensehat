#!/bin/bash

echo "Installing Binday Sense HAT system..."

sudo apt update
sudo apt install -y python3-sense-hat python3-pip

pip3 install python-dateutil

mkdir -p logs data

echo "Done."
echo "Run with: python3 src/main.py"
