from random import randint
def cut(n: int) -> bool: return n%2==0
say = int(input("How many elements: "))
if say%3==0:
    massiv = [randint(10, 99) for _ in range(say)]
    print("List =", massiv)
    cut_index, cem = -1, 0
    for i in range(say):
        if cut(massiv[i]):
            cut_index = i
            break
        else: cem += massiv[i]
    if cut_index==-1: print(f"Massivde cut element yoxdur\nCem: {cem}")
    else: print(f"Listin ilk cut elementi: A[{cut_index}] = {massiv[cut_index]}\nCem: {cem}")
    b = []
    for i in range(0, say, 3): b += [(*massiv[i:i+3],)]
    print("B:", b)
else: print("3-e bolunen eded daxil edin.")