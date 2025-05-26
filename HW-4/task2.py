def length_num(number: int) -> int:
    say = 0
    while number>0:
        say+=1
        number//=10
    return say

def is_polydivisible(number: int, length: int) -> bool:
    flag = True
    for i in range(length):
        res = number//(10**(length-i-1))%(i+1)
        print(f"{number//(10**(length-i-1))} % {i+1} = {res}")
        if res: flag = False
    return flag
eded = int(input("Enter a number (N>0): "))
print(is_polydivisible(eded, length_num(eded)))
