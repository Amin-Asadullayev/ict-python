def length_num(number: int) -> int:
    say = 0
    while number>0:
        say+=1
        number//=10
    return say

def look_and_say(number: int) -> str:
    result = ""
    for i in range(0, length_num(number), 2):
        current = number%100
        number//=100
        result = (f"{current%10}"*(current//10)) + result
    return result

eded = int(input("Enter a number (N>0): "))
if length_num(eded)%2: print("invalid")
else: print(look_and_say(eded))