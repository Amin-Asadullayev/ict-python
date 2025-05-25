print("{:15s} {:15s}".format("Celcius", "Fahrenheit"))
for i in range(0, 101, 10): print("{:<15d} {:<15.0f}".format(i, i*9/5+32))