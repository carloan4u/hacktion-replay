#!/bin/sh
sudo raspivid -c -o /home/pi/hacktionreplay.h264 -s -t 30000 -b 10000000 --nopreview
