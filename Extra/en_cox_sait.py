dij = {
    "a": 0,
    "e": 0,
    "ə": 0,
    "i": 0,
    "o": 0,
    "ö": 0,
    "u": 0,
    "ü": 0
}
setir = input("Giriş: ")
for i in setir:
    if i in "aeəioöuü": dij[i]+=1
mx = "a"
for i in dij:
    if dij[i]>dij[mx]: mx=i
print(f"Çıxış: {mx}")