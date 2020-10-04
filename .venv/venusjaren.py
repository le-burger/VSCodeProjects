# Leander Burger | Programma voor het berekenen van huidige leeftijd en de leeftijd in venusjaren.
import datetime

# Input ophalen.
naam = input('Wat is je naam?')
geboortejaar = int(input('Dankje, en wat is je geboortejaar?'))

# Berekening van leeftijden.
ditJaar = datetime.date.today().year
leeftijd = ditJaar - geboortejaar

venusMultiplyer = 1.62
venusJaren = leeftijd * venusMultiplyer

# Output geven.
print(f"Beste, {naam} in {ditJaar} is je leeftijd op aarde {leeftijd}.")
print(f"En je leeftijd is dan {venusJaren} in Venusjaren.")