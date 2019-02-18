echo "1" > /sys/class/gpio/gpio18/value
play ./aprs_reply/process_convert_sstv.wav 
echo "0" > /sys/class/gpio/gpio18/value
python -m pysstv ./capture/$1 output.wav --mode $2

echo "1" > /sys/class/gpio/gpio18/value
play output.wav
echo "0" > /sys/class/gpio/gpio18/value


