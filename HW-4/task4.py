def is_Palindrome(number: int) -> bool:
    new_number, temp = 0, number
    while temp>0:
        new_number = new_number*10+temp%10
        temp//=10
    return new_number==number

def to_Binary(number: int) -> str:
    binary = ""
    if not number: return "0"
    while number>0:
        binary = f"{number%2}{binary}"
        number//=2
    return binary

def Palindrome_type(number: int) -> str:
    binary = to_Binary(number)
    if binary==binary[::-1] and is_Palindrome(number): return "Palindrome type is Decimal and Binary"
    elif is_Palindrome(number): return "Palindrome type is only Decimal"
    elif binary==binary[::-1]: return "Palindrome type is only Binary"
    else: return "Palindrome type is neither Decimal nor Binary"

number = int(input("Enter a number (N>0): "))
print(f"Decimal: {number}\nBinary: {to_Binary(number)}\n{Palindrome_type(number)}")