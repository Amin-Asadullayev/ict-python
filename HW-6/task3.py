numbers, say, cem = [], 0, 0
while True:
    num = input("Enter a number[blank to quit]: ")
    if num==" ": break
    else:
        numbers += [(num:=int(num))]
        say, cem = say+1, cem+num
print("A list of numbers:", numbers)
print("Average value:", (avrg:=cem/say))
lta, avr, hta = [], [], []
for i in numbers:
    if i<avrg: lta+=[i]
    elif i>avrg: hta+=[i]
    else: avr+=[i]
print("Less than Average:", *lta)
print("Average:", *avr)
print("Higher than Average:", *hta)