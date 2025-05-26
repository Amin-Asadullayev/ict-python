allof, even, odd = [],[],[]
while True:
    if (num:=input("Enter a number[blank to quit]: "))!=" ":
        allof += [(num:=int(num))]
        if num%2: odd+=[num]
        else: even+=[num]
    else: break
print(allof)
print(f"Evens: {even}\nOdds: {odd}")
