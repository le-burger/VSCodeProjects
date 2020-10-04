# Leander Burger | Programma voor het raden van getallen. 
import random

# Minimale en maximale input waardes en vervolgens random getal genereren
min = int(input("Voer de minimum waarde in van het raad-getal:"))
max = int(input("Voer de maximum waarde in van het raad-getal:"))

getal = random.randrange(min, max)

# Aantal pogingen tussen de 1 en 5 invoeren
pogingen = int(input("Hoe vaak mag er geraden worden [1-5]"))

while pogingen < 1 or pogingen > 5: 
    print("Je mag alleen een getal van 1 tot en met 5 invoeren.")
    pogingen = int(input("Hoe vaak mag er geraden worden [1-5]"))

# Getal raden en terugkoppeling geven 
lijst = []
x = 0

while x < pogingen:
    raadPoging = int(input("Raad het raad-getal:"))
    if raadPoging == getal:
        print("succes!")
        lijst.append(str(raadPoging) + " succes!")
        join = ", ".join(lijst)
        print(f"Gefeliciteerd! Hieronder een overzicht van uw invoer: {join}")
        break
    elif raadPoging < getal:
        print("te laag")
        lijst.append(str(raadPoging) + " te hoog")
    else:
        print("te hoog")
        lijst.append(str(raadPoging) + " te laag")
    x += 1