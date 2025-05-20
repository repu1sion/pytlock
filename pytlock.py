#!/usr/bin/python3

import time
import sys
import os

ver='0.14'

#select xdg-screensaver or xscreensaver to use. if 0 - xscreensaver, 1 - xdg
XDG_SCREENSAVER = 0


minutes = 20                        # default value
seconds = minutes*60

def print_time():
    os.system('clear')
	#reduce flickering with redrawing cursor
    #os.system('printf \'\033[;H\'')
    print(pyt_time)

# ----- main -----
print('pytlock started. ver:', ver, 'args:', len(sys.argv))
#print(sys.argv[1])

# check args
if (len(sys.argv) > 1):
    # if 't' is input - lock in 2 secs for test
    if (sys.argv[1] == 't'):
        seconds = 2
    elif (sys.argv[1] == 'h'):
        print('usage: pytlock [time] . default value 20 mins. t - test, h - help')
        sys.exit(0)
    else:
        minutes = int(sys.argv[1])
        seconds = minutes*60
        if (minutes == 0):
            sys.exit(0)

# clear screen for a first time
os.system('clear')

while True:
    # 1. get mins:secs to show
    show_mins = int(seconds/60)
    show_secs = seconds%60

    # 2. form string with time to show
    pyt_time = str(show_mins)    
    pyt_time += ":"
    if (show_secs < 10):
        pyt_time += "0"
    pyt_time += str(show_secs)    

    # 3. show
    print_time()

    # 4. time is over - exit!
    # seconds contain everythin!
    if (seconds == 0):
        print_time()
        print('your time is over!')
        if (XDG_SCREENSAVER == 1):
            os.system('xdg-screensaver lock')
        else: #blanking screen, not locking
            os.system('xscreensaver-command -activate')
        time.sleep(1) 
        sys.exit(0)

    # 5. sleep and math
    time.sleep(1)
    if (seconds > 0):
        seconds -= 1
