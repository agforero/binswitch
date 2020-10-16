#/usr/bin/bash

echo -e "00000000000000000000000000000000\t00000000000000000000000000000000" > data.txt
python input.py &
python outputDisplay.py &