month, day = input("Enter a month [ex. March]: "), int(input("Enter the day [ex. 12]: "))
if month=="December": sign = "invalid" if day>=31 else"Capricorn" if day>=22 else "Sagittarius" 
elif month=="January": sign = "invalid" if day>=31 else"Aquarius" if day>=20 else "Capricorn"  
elif month=="February": sign = "invalid" if day>=28 else"Pisces" if day>=19 else "Aquarius"
elif month=="March": sign = "invalid" if day>=31 else"Aries" if day>=21 else "Pisces"  
elif month=="April": sign = "invalid" if day>=30 else"Taurus" if day>=20 else "Aries"  
elif month=="May": sign = "invalid" if day>=31 else"Gemini" if day>=21 else "Taurus"   
elif month=="June": sign = "invalid" if day>=30 else"Cancer" if day>=21 else "Gemini"  
elif month=="July": sign = "invalid" if day>=31 else"Leo" if day>=23 else "Cancer"  
elif month=="August": sign = "invalid" if day>=31 else"Virgo" if day>=23 else "Leo"  
elif month=="September": sign = "invalid" if day>=30 else"Libra" if day>=23 else "Virgo"  
elif month=="October": sign = "invalid" if day>=31 else"Scorpio" if day>=23 else "Libra"  
elif month=="November": sign = "invalid" if day>=30 else"Sagittarious" if day>=22 else "Scorpio"  
else: sign = "invalid"
if sign=="invalid": print("Either a month or a day is invalid!")
else: print(f"Your zodiac sign is {sign}")