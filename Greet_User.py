import datetime

hour = datetime.datetime.now().hour
if hour >= 0 and hour <=12:
    print("Good Morning,Sir!")
elif hour > 12 and hour <= 17:
    print("Good Afternoon,Sir!")
elif hour > 17 and hour <= 20:
    print("Good Evening,Sir!")
else:
    print("Good Night,Sir!")

