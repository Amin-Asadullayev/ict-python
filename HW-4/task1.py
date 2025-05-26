def max_collatz(number: int) -> int:
    mx = number
    while number>1:
        print(f"{number:.0f}", end=" ")
        number = number*3+1 if number%2 else number/2
        if number>mx: mx = number
    print(1)
    return mx
print(f"Max number: {max_collatz(int(input('Enter a number (N>0): '))):.0f}")