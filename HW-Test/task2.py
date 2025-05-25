from math import pi, sin
a, b, angle = float(input('Side 1: ')), float(input('Side 1: ')), float(input('Angle(degree): '))
print(f"\nArea: {(0.5*a*b*sin(angle*pi/180)):.2f}")