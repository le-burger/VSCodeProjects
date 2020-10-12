# Auteur: Leander Burger 
# Groep: ID1G1
# Eindopdracht
# Op basis van de ingevoerde vakken, te behalen studiepunten en de einddatum opleiding
# zal dit programma aantonen hoeveel procent er is afgerond en hoelang de opleiding nog duurt.

from openpyxl import Workbook
from datetime import datetime, date

print("Met dit programma is het mogelijk om de voortgang van je studie in te zien. Door alle vakken, type") 
print("punten en de einddatum in te voeren geeft dit programma de voortgang aan. \n")

# Gather input: all fields and its receivable points
isThatAll = "N"
FIELD_COLUMN = 1
POINTS_COLUMN = 1


wb = Workbook()
sheet = wb.active

while isThatAll == "N":
    field = input("Wat is de naam van het vak?")
    sheet['A'  + str(FIELD_COLUMN)] = field
    FIELD_COLUMN += 1

    points = int(input(f"Hoeveel punten zijn er te behalen voor {field}?"))
    sheet['B'  + str(POINTS_COLUMN)] = points
    POINTS_COLUMN += 1

    isThatAll = input("Zijn alle vakken ingevoerd? (Y/N)").upper()

wb.save('.venv\studycourse.xlsx') 

# Ask for the enddate of the study and validate the date.
def checkDate(date):
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False

endDate = input("Please enter the end date of your study dd-mm-yyyy")

while checkDate(endDate) == False:
    endDate = input("Please enter a valid date. Format: dd-mm-yyyy")


# Compare dates and show calculate the difference. If no list use: endDateList = endDate.split('-')
endDateObj = datetime.strptime(endDate, "%d-%m-%Y")
today = date.today()
future = date(endDateObj.year,endDateObj.month,endDateObj.day)
diff = future - today
print (diff.days)