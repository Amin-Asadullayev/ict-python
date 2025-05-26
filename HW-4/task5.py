def length_num(number: int) -> int:
    say = 0
    while number>0:
        say+=1
        number//=10
    return say

def np_to_k(num: int, pos: int) -> int:
    temp, cem = num, 0
    for i in range(length_num(num)-1, -1, -1):
        cem += (temp%10)**(pos+i)
        temp//=10
    res = cem/num
    return int(res) if int(res)==res else None

n, m = int(input("Enter N: ")), int(input("Enter M: "))
print("K:", np_to_k(n,m))