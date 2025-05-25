n = input("Max number to compute the average value: ")
for i in n:
    if not("0"<=i<="9"):
        flag = True
        break
else: flag = False
if flag or int(n)<=0: print("Error message")
else:
    cem, n = 0, int(n)
    for i in range(1, n+1): cem+=int(input(f"Value {i}: "))
    print("Average value: {:.2f}".format(cem/n))
