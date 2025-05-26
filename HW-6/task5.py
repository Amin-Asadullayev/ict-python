def sum_of_elements(coor: list) -> float:
    cem = 0
    for i in coor: cem+=i
    return cem

def multiplication(x_data: list, y_data: list) -> list:
    j, mul = 0, []
    for i in x_data:
        mul += [i*y_data[j]]
        j+=1
    return mul

x, y = [], []
for i in range(1, 4):
    x_, y_ = map(float, input(f"Enter x{i},y{i}: ").split())
    x += [x_]
    y += [y_]
print("X coordinates:", x)
print("Y coordinates:", y)
m = (sum_of_elements(multiplication(x, y))-(sum_of_elements(x)*sum_of_elements(y))/3)/(sum_of_elements([i**2 for i in x])-((sum_of_elements(x)**2)/3))
b = sum_of_elements(y)/3-m*sum_of_elements(x)/3
print(f"f(x) = {m:.2f} * x {'-' if b<0 else '+'} {abs(b):.2f}")