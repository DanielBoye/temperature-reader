# Imports go at the top
from microbit import *

data = []

# Writes data 144 times to the array called data
while len(data) < 144:
    data.append(temperature())
    # Sleeps in 5 minutes (in milliseconds)
    sleep(300000) 

# Write the 144 temperature readings in a temp.dat file
with open('temp.dat', 'w') as min_fil:
    for i in data:
        min_fil.write(str(i))
        min_fil.write(',')

display.show(Image.HAPPY)
