month, day = input("Enter name of the month [ex. June]: "), int(input("Enter the day [ex. 5]: "))
if month == "March":
    season = "Spring" if day>=20 else "Winter"
elif month == "June":
    season = "Summer" if day>=21 else "Spring"
elif month == "September":
    season = "Fall" if day>=22 else "Summer"
elif month == "December":
    season = "Winter" if day>=21 else "Fall"
elif month in ["April", "May"]: season = "Spring"
elif month in ["July", "August"]: season = "Summer"
elif month in ["October", "November"]: season = "Fall"
else: season = "Winter"
print(f"{month} {day} is in {season}")