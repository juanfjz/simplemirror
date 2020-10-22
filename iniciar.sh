#!/bin/bash
cd $(dirname $0)
python programa.py &
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk index.html &
