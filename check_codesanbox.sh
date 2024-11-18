#/bin/sh

COORDINATE_CLOSE_TAB="252 46"
COORDINATE_OPEN_TAB="141 46"

start_container=1
end_container=8

while [ $start_container -le $end_container ]
do

    xdotool mousemove $COORDINATE_OPEN_TAB click 1
    xdotool click 3
    sleep 1

    xdotool key --repeat 7 Down key Right
    sleep 1

    xdotool key --repeat $start_container Down key Return
    sleep 7

    echo "container $((start_container + 1)) is open now!"

    xdotool mousemove $COORDINATE_CLOSE_TAB click 1
    sleep 2

    # 😎 repeat next step... 
    ((start_container++))
done