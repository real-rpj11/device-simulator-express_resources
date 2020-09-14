"""This example lights up all the NeoPixel LEDs red."""
from adafruit_circuitplayground import cp
# import CPX library
from adafruit_circuitplayground import cp
from time import sleep

cp.pixels.brightness = 1
index = 9
while True:
    if cp.switch:
        if index > 9 :
            index = 0
        else:
            cp.pixels[index] = (50,0,0)
            sleep(0.5)
            cp.pixels[index] = (0, 0, 0)
            sleep(0.5)
            index+= 1
            
    else :
        if index < 0:
            index = 9
        else:
            cp.pixels[index] = (50,0,0)
            sleep(0.5)
            cp.pixels[index] = (0, 0, 0)
            sleep(0.5)
            index-= 1

        