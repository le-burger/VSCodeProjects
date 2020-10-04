# Leander Burger | Eindopdracht | Op basis van de ingevoerde vakken, te behalen studiepunten en de einddatum opleiding
# zal dit programma aantonen hoeveel procent er is afgerond en hoelang de opleiding nog duurt.
import openpyxl

print("Met dit programma is het mogelijk om de voortgang van je studie in te zien. Door alle vakken, type") 
print("punten en de einddatum in te voeren geeft dit programma de voortgang aan. \n")

# Gather input: all fields and its receivable points and the enddate of the course
isThatAll = "N"
fieldColumn = 1
pointsColumn = 1

wb = openpyxl.load_workbook('example2.xlsx')
sheet = wb['Sheet1']

while isThatAll == "N":
    field = input("Wat is de naam van het vak?")
    sheet['A'  + str(fieldColumn)] = field
    fieldColumn += 1

    points = input(f"Hoeveel punten zijn er te behalen voor {field}?")
    sheet['B'  + str(pointsColumn)] = points
    pointsColumn += 1

    wb.save('example2.xlsx')
    isThatAll = input("Zijn alle vakken ingevoerd? (Y/N)").upper()

endDate = input("Wanneer is de einddatum van de opleiding?")