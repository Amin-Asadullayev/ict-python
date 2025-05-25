iller, year = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare", "Dragon", "Snake", "Horse", "Sheep"], int(input("Enter the year [ex. 2021]: "))
if year<0: print("Invalid year!")
else: print(f"{year} is the year of the {iller[year%12]}")