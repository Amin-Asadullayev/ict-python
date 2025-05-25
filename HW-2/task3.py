wl = int(input("Enter the wavelength in nm: "))
if wl<380 or wl>750: print("Invalid input!")
else:
    if 380<=wl<450: color = "Violet"
    elif 450<=wl<495: color = "Blue"
    elif 495<=wl<570: color = "Green"
    elif 570<=wl<590: color = "Yellow"
    elif 590<=wl<620: color = "Orange"
    elif 620<=wl<=720: color = "Red"
    print(f"The relevant color is {color}")