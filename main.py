# Imports go at the top
from microbit import *

data = []

# Code in a 'while True:' loop repeats forever
while len(data) < 144:
    data.append(temperature())
    sleep(300)

with open('temp.dat', 'w') as min_fil:
    for i in data:
        min_fil.write(str(i))
        min_fil.write(',')

display.show(Image.HAPPY)
