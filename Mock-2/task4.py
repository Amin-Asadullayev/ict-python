def len(massiv: list) -> int:
    say = 0
    for i in massiv: say+=1
    return say
def selection_sort(massiv: list) -> list:
    massiv = [*massiv] # Shallow copy
    for i in range(len(massiv)):
        min = i
        for j in range(i, len(massiv)):
            if massiv[j]<massiv[min]: min = j
        if i!=min: massiv[i], massiv[min] = massiv[min], massiv[i]
    return massiv

massiv = []
while True:
    eded = input("Enter a number['end' to quit]: ")
    if eded=="end": break
    else:
        massiv+=[int(eded)]
print("Massiv:", *massiv )
print("Sortlanmis massiv:", *selection_sort(massiv))
             