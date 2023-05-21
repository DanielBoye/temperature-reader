from microbit import *

data = []

# Skrive data 12 ganger til en array som heter data
while len(data) < 12:
    data.append(temperature())
    # Sove i 1 time
    sleep(3600000) 

# Skrive de 12 temperatur avlesningene i en temp.dat fil
with open('temp.dat', 'w') as min_fil:
    for i in data:
        min_fil.write(str(i))
        min_fil.write(',')

display.show(Image.HAPPY)
