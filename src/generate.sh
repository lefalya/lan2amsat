echo -n "YB3MBN>WORLD:$1" | gen_packets -a 25 -o x.wav - 
play x.wav 
unlink x.wav

