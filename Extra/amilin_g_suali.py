setir, numbers = input("Setiri daxil ele, a bala: "), []
for i in range(len(setir)):
    say = 1
    for j in range(len(setir)):
        if setir[i]>setir[j] or (setir[i]==setir[j] and i>j): say+=1
    numbers.append(say)
print(numbers)