#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import RPi.GPIO as gpio
import time

#set up pin 17 as an input
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
		input_value = gpio.input(17)
		if input_value == False:
				print('The Button has been pressed!')
				time.sleep(0.2)
				#while input_value == False:
						#input_value = gpio.input(17)

