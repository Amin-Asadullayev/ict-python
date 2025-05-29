from random import randint
def len(a) -> int:
    say = 0
    for _ in a: say+=1
    return say
def abs(a: int): return -a if a<0 else a
def selection_sort(massiv: list) -> list:
    massiv = [*massiv]
    for i in range(len(massiv)):
        mn = i
        for j in range(i, len(massiv)):
            if massiv[j]<massiv[mn]: mn = j
        if mn!=i: massiv[i], massiv[mn] = massiv[mn], massiv[i]
    return massiv

def binary_search(massiv: list, target: int) -> int:
    L, R = 0, len(massiv)-1
    while L<=R:
        mid = (L+R)//2
        if massiv[mid]==target:
            return mid
        elif massiv[mid]<target:
            L = mid+1
        elif massiv[mid]>target:
            R = mid-1
    return mid

massiv = [randint(1, 20) for _ in range(9)]
print("Massiv:", *massiv)
massiv = selection_sort(massiv)
print("Cesidlemeden sonra:", *massiv)
x = int(input("X ededi daxil edin: "))
result = binary_search(massiv, x)
if massiv[result]==x:
    print(f"{x} ededi tapildi")
else:
    dgr = (result - (1 if massiv[result]>x else -1))%len(massiv)
    print(f"{x} ededi tapilmadi. En yaxin eded: {massiv[result] if abs(massiv[result]-x)<abs(massiv[dgr]-x) else massiv[dgr]}")
        