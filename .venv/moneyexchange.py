# Leander Burger | Programma voor het inwisselen dollars, ponden en yen naar euro's.

# Wisselkoers
POND = 1.08
DOLLAR = 0.84
YEN = 0.0080

# Input: keuze van valuta en in te wisselen bedrag
wisselValuta = input("Valuta (1 = US dollar, 2 = GB pounds, 3 = Yen):")
valuta = ""

while wisselValuta != "1" and wisselValuta != "2" and wisselValuta != "3":
    print("Ongeldige keuze.")
    wisselValuta = input("Valuta (1 = US dollar, 2 = GB pounds, 3 = Yen):")
    if wisselValuta == "1":
        wisselValuta = DOLLAR
        valuta = "US dollar"
        break
    elif wisselValuta == "2":
        wisselValuta = POND
        valuta = "Britse pond"
        break
    elif wisselValuta == "3":
        wisselValuta = YEN
        valuta = "Japanse yen"
        break

if wisselValuta == "1":
    wisselValuta = DOLLAR
    valuta = "US Dollar"
elif wisselValuta == "2":
    wisselValuta = POND
    valuta = "Britse pond"
elif wisselValuta == "3":
    wisselValuta = YEN
    valuta = "Japanse yen"

bedrag = float(input("In te wisselen bedrag:"))

# Berekening van wisselbedrag en transactiekosten 
wisselBedrag = bedrag * wisselValuta
round(wisselBedrag, 2)

TRANSACTIE_PERCENTAGE = 0.015
transactieKosten = wisselBedrag * TRANSACTIE_PERCENTAGE
round(transactieKosten, 2)

if transactieKosten < 2:
    transactieKosten = 2
elif transactieKosten > 15:
    transactieKosten = 15

teOntvangenBedrag = wisselBedrag - transactieKosten
round(teOntvangenBedrag, 2)

# Output valuta naar euro transactiekosten afgetrokken
print(f"Voor {bedrag} {valuta} krijgt u {wisselBedrag}. De transactiekosten bedragen € {transactieKosten} U ontvangt €{teOntvangenBedrag}")