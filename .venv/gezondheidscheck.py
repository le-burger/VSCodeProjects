# Leander Burger | program which asks for health stats and returns if these are healthy values.  

# function used to check stats
def isTussen(value, minimum, maximum):
    if value >= minimum and value <= maximum:
        return True
    else:
        return False

# minimum and maximum health stat values
MAX_HR = 90
MIN_HR = 55

MAX_TEMP = 37.5
MIN_TEMP = 36.3

MAX_HG = 140
MIN_HG = 100

# asking for input from the user
userHeartRate = int(input("What is your current heartrate?"))
userTemperature = int(input("What is your current temperature?"))
userBloodpressure = int(input("What is your current bloodpressure?"))

# stats are used below to check if user is healthy  
healthyHeartRate = isTussen(userHeartRate, MIN_HR, MAX_HR)
healthyTemperature = isTussen(userTemperature, MIN_TEMP, MAX_TEMP)
healthyBloodpressure = isTussen(userBloodpressure, MIN_HG, MAX_HG)

if healthyHeartRate: 
    print("You have a healthy heart rate!")
else:
    print("Heart rate is to low. Go see the doctor")

if healthyTemperature: 
    print("You have a healthy temperature!")
else:
    print("Temperature is to low. Go see the doctor")

if healthyBloodpressure: 
    print("You have a healthy blodpressure!")
else:
    print("Bloodpressure is to low. Go see the doctor")