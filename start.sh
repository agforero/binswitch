#/usr/bin/bash

echo -e "00000000000000000000000000000000\t00000000000000000000000000000000" > data.txt
python3 input.py &
python3 outputDisplay.py &