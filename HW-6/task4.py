prev = curr = int(input("Enter a number[blank to quit]: "))
desc, asc = True, True
while True:
    num = input("Enter a number[blank to quit]: ")
    if " "==num or num=="": break
    else:
        prev, curr = curr, int(num)
        if prev>curr: asc = False
        if curr>prev: desc = False
print("A list is ascendingly sorted" if asc else "A list is descendingly sorted" if desc else "A list is unsorted")
