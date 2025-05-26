from random import randint
def my_function(my_list: list) -> tuple:
    new_list, count = [], 0
    for n in my_list:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                count += 1
                break
        else: new_list += [n]
    return new_list, count

massiv = [randint(10, 99) for _ in range(20)]
print("List:", massiv)
cavab = my_function(massiv)
print(f"Prime number list: {cavab[0]}\nNumber of non-prime numbers: {cavab[1]}")