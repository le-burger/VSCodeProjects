# Auteur: Leander Burger 
# Group: ID1G1
# Eindopdracht
# This program will show the progress of your study after collecting some data through questions.

from openpyxl import Workbook
from datetime import datetime, date
import time
import sys

# Gathering the school data from the user.
print("This program will show you the progress of your study after collecting some data through questions.") 

isThatAll = "N"
column = 1

wb = Workbook()
sheet = wb.active

while isThatAll == "N":
    field = input("What's the name of the course?")
    sheet['A'  + str(column)] = field
    points = int(input(f"How many studypoints can you get for {field}?"))
    sheet['B'  + str(column)] = points
    passed = input(f"Did you already pass {field} (Y/N)?").upper()
    sheet['C'  + str(column)] = passed
    column += 1

    isThatAll = input("Did you fill in all courses? (Y/N)").upper()

wb.save('studycourse.xlsx') 

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

# Making arrays from the rows in excel sheets to use from 
courses = sheet['A']
studyPoints = sheet['B']
passedCourse = sheet['C']

courseArray = [] 
studyPointsArray = [] 
passedPointsArray = []

x = 0
for i in courses:
    courseArray.append(courses[x].value)
    studyPointsArray.append(studyPoints[x].value)
    if passedCourse[x].value == 'Y':
        passedPointsArray.append(studyPoints[x].value)
    x += 1

# Calculating time left for getting all points using datetime module
endDateObj = datetime.strptime(endDate, "%d-%m-%Y")
today = date.today()
future = date(endDateObj.year,endDateObj.month,endDateObj.day)
difference = future - today

# Function to calculate the progress
def progress(total, passed):
    totalPoints = sum(total)
    passedPoints = sum(passed)
    PERCENTAGE = 100
    return (passedPoints / totalPoints) * PERCENTAGE

# Output in a friendly way
def normal_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

# Output to user
normal_print(f"After meticulously calculating and checking the gathered data I've came to the conclusion that your progress to completion so far is {progress(studyPointsArray, passedPointsArray)}%!")
slow_print(".....")
normal_print(f"No worries though you still have {difference.days} days left to get to 100%!")