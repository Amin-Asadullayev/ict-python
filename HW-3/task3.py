def strip(setir: str) -> str:
    for i1 in range(len(setir)):
        if setir[i1]!=" ": break
    for i2 in range(len(setir)-1, -1, -1):
        if setir[i2]!=" ": break
    return setir[i1:i2+1]
qiymet = {
    "A+": 4,
    "A": 4,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1,
    "F": 0
}
cem, say = 0,0
while True:
    response = input("Enter the grade('end' to quit): ")
    if response=="end": break
    cem+=qiymet[strip(response)]
    say+=1
print("\nA grade point average: {:.1f}".format(cem/say if say else 0))
