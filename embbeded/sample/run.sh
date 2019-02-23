#!/usr/bin/env bash
source "../bin/activate"

if [[ -n $PRODUCTION ]]; then 
    echo "18" > /sys/class/gpio/export 
    echo "out" > /sys/class/gpio/direction 
fi
direwolf &
python main.py
