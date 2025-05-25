ilk = prev = curr = (float(input("Enter the x part of the coordinate: ")), float(input("Enter the y part of the coordinate: ")))
mesafe = 0
while True:
    if (x := input("Enter the x part of the coordinate ('end' to quit): "))=="end": break
    y = float(input("Enter the y part of the coordinate: "))
    prev, curr = curr, (float(x), y)
    mesafe+=((curr[0]-prev[0])**2+(curr[1]-prev[1])**2)**0.5
mesafe+=((curr[0]-ilk[0])**2+(curr[1]-ilk[1])**2)**0.5
print(f"The perimeter of that polygon is {mesafe:.2f}")