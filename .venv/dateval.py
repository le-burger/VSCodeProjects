import datetime

endDate = input("Wat is de datum?")

def checkDate(date):
    try:
        datetime.datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False

print(checkDate(endDate))

