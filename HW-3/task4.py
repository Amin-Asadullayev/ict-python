def strip(setir: str) -> str:
    for i1 in range(len(setir)):
        if setir[i1]!=" ": break
    for i2 in range(len(setir)-1, -1, -1):
        if setir[i2]!=" ": break
    return setir[i1:i2+1]
qiymet = 0
while True:
    if strip(cenab := input("Enter the age of guest ('end' to quit): "))=="end": break
    qiymet+= 0 if (cenab:=int(cenab))<=2 else 14 if 3<=cenab<=12 else 18 if cenab>=65 else 23
print(f"The total for that group is ${qiymet:.2f}")