kilo = {"alma" :  8 ,
        "uzum" :  12,
        "hurma" : 18,
        "banan" : 25,
        "nar" : 15 }

for i, j in kilo.items():
    print(i, "-" ,j, 'manat')
sum = 0 
while True:
    isleg = input("Name almak isleyarsiniz?: ")
    if isleg == "quit":
        break
    elif isleg in kilo:
        kg = float(input("Nace almak isleyarsiniz?: "))
        pul = kg * kilo[isleg]
        sum += pul 
print(f"Siz {sum} manat tolemeli")
       