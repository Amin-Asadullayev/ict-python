a, b = int(input("A: ")), int(input("B: "))
if a<b:
    massiv, yeni_massiv = [i for i in range(a, b)], []
    for i in massiv:
        temp, cem, ters = i, 0, 0
        while temp>0:
            cem += temp%10
            temp //= 10
        while cem>0:
            ters = ters*10+cem%10
            cem//=10
        if not i%ters: yeni_massiv.append(i)
    print(yeni_massiv)
else:
    print("Intervali duzgun daxil ediniz.")