a, b = int(input("A: ")), int(input("B: "))
if a<b:
    massiv, yeni_massiv = [i for i in range(a, b)], []
    for i in massiv:
        temp, hasil, ters_hasil = i, 0, 0
        while temp>0:
            hasil += temp%10
            temp //= 10
        temp = hasil
        while temp>0:
            ters_hasil = ters_hasil*10+temp%10
            temp //= 10
        if hasil*ters_hasil==i: yeni_massiv.append(i)
    print(yeni_massiv)
else:
    print("Intervali duzgun daxil ediniz.")