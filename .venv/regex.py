import re
import datetime

def yield_valid_dates(dateStr):
    for match in re.finditer(r"\d{1,2}-\d{1,2}-\d{4}", dateStr):
        try:
            date = datetime.datetime.strptime(match.group(0), "%m-%d-%Y")
            yield date
            # or you can yield match.group(0) if you just want to
            # yield the date as the string it was found like 05-04-1999
        except ValueError:
            # date couldn't be parsed by datetime... invalid date
            pass
    print(date)
    


testStr = input("wat is de datum?")

yield_valid_dates(testStr)

#print(date)
