A = int(input("Enter Side A: "))
B = int(input("Enter Side B: "))
C = int(input("Enter Side C: "))
D = int(input("Enter Side D: "))
E = int(input("Enter Side E: "))

def five_sides(A,B,C,D,E):
    F = (D-(B+E))
    G = (A-C)
    return (A*B)+(F*G)+((E*G)/2)

print(five_sides(A,B,C,D,E))

