var=`date -u` 
echo $var
echo -n "WB2OSZ>WORLD:LOOPBACK;${var}" | gen_packets -a 25 -o x.wav -
play x.wav

