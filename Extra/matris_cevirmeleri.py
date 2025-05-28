from random import randint

def matris_print(matris: list):
    for i in matris:
        for j in i:
            print(f"{j:<5d}", end="")
        print()

def derece90(matris: list, olcu: int) -> list:
    matris90 = [[0 for _ in range(olcu)] for _ in range(olcu)]
    for i in range(olcu):
        for j in range(olcu):
            matris90[j][olcu-i-1] = matris[i][j]
    return matris90

def derece180(matris: list, olcu: int) -> list:
    matris180 = [[0 for _ in range(olcu)] for _ in range(olcu)]
    for i in range(olcu):
        for j in range(olcu):
            matris180[olcu-1-j][i] = matris[j][i]
    return matris180

def derece270(matris: list, olcu: int) -> list:
    matris270 = [[0 for _ in range(olcu)] for _ in range(olcu)]
    for i in range(olcu):
        for j in range(olcu):
            matris270[olcu-1-j][i] = matris[i][j]
    return matris270

n = int(input("N: "))
matris = [[randint(10, 99) for _ in range(n)] for _ in range(n)]
matris_print(matris)
print()
matris_print(derece270(matris, n))
