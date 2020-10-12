# Auteur: Leander Burger 
# Groep: ID1G1
# Eindopdracht
# This program will show the progress of your study after collecting some data through questions.

from openpyxl import Workbook
from datetime import datetime, date

print("This program will show you the progress of your study after collecting some data through questions.") 

isThatAll = "N"
FIELD_COLUMN = 1
POINTS_COLUMN = 1

wb = Workbook()
sheet = wb.active

while isThatAll == "N":
    field = input("What;s the name of the course?")
    sheet['A'  + str(FIELD_COLUMN)] = field
    FIELD_COLUMN += 1

    points = int(input(f"how many studypoints can you get for {field}?"))
    sheet['B'  + str(POINTS_COLUMN)] = points
    POINTS_COLUMN += 1

    isThatAll = input("Did you fill in all courses? (Y/N)").upper()

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

# Making arrays from the rowa in excel sheets
COURSES = sheet['A']
courseArray = [] 
x = 0

for i in COURSES:
    courseArray.append(COURSES[x].value)
    x += 1

STUDYPOINTS = sheet['B']
studyPointsArray = [] 
y = 0 

for i in STUDYPOINTS:
    studyPointsArray.append(STUDYPOINTS[y].value)
    y += 1

print(courseArray)
print(studyPointsArray)

# Compare dates and show calculate the difference. If no list use: endDateList = endDate.split('-')
endDateObj = datetime.strptime(endDate, "%d-%m-%Y")
today = date.today()
future = date(endDateObj.year,endDateObj.month,endDateObj.day)
diff = future - today
print (diff.days)

# TBD, sum of studyPointsArray, check on passed courses, output percentage of collected point and days left to get to 100%