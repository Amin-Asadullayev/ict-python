from random import randint
def len(a) -> int:
    say = 0
    for _ in a: say+=1
    return say

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
    return -1

massiv = [randint(1, 10) for _ in range(9)]
print("Massiv:", *massiv)
massiv = selection_sort(massiv)
print("Cesidlemeden sonra:", *massiv)
x = int(input("X ededi daxil edin: "))
result = binary_search(massiv, x)
if result==-1:
    print(f"{x} ededi tapilmadi")
else:
    L, R, say = result-1, result+1, 1
    while massiv[L]==x or massiv[R]==x:
        if massiv[L]==x:
            say, L = say+1, L-1
        if massiv[R]==x:
            say, R = say+1, R+1
    print(f"{x} ededi {say} defe tekrarlanir")
        