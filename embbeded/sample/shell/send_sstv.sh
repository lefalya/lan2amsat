if [[ -n $PRODUCTION ]]; then 
    echo "1" > /sys/class/gpio/gpio18/value
fi

play ./aprs_reply/process_convert_sstv.wav 

if [[ -n $PRODUCTION ]]; then 
    echo "0" > /sys/class/gpio/gpio18/value
fi 

python -m pysstv ./capture/$1 output.wav --mode $2

if [[ -n $PRODUCTION ]]; then 
    echo "1" > /sys/class/gpio/gpio18/value
fi

play output.wav

if [[ -n $PRODUCTION ]]; then 
    echo "0" > /sys/class/gpio/gpio18/value
fi


