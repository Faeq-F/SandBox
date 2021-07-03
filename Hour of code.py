from datetime import datetime, timedelta
currentTimeFormatted = datetime.now()
timeNeeded = input("""Please enter the number of hours required """)
expiredTime = currentTimeFormatted + timedelta(hours=int(timeNeeded))
if int(timeNeeded) <= 2:
    charge = "3.50"
elif int(timeNeeded) <= 4 and int(timeNeeded) > 2:
    charge = "5.00"
elif int(timeNeeded) <= 12 and int(timeNeeded)> 4:
    charge = "10.00"
else:
    print("There was an error")

print("""Time now:\t""",currentTimeFormatted,"""\nExpires:\t""",expiredTime,"\nCharge = £",charge)