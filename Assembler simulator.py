file = str(input("Unesite ime file-a: "))
file += ".txt"
redovi = []
with open(file, "r") as f:
    for red in f:
        redovi.append(red)
for i in range(len(redovi) - 1):
    redovi[i] = redovi[i][:-1]

varijable = {}
varijabla = ""
broj_varijabli = int(input("Unesite broj varijabli u programu: "))
print()
for i in range(broj_varijabli):
    ime_varijable = str(input("Unesite ime varijable: "))
    vrijednost_varijable = int(input("Unesite vrijednost varijable: "))
    varijable[ime_varijable] = vrijednost_varijable
    print()

komande = ["LOAD", "LC", "STORE", "ADD", "BNEG", "SUB", "MUL", "DIV"]
linija_koda = 0
oznaka = ""
akumulator = 0

znak = 0
while True:
    string = ""
    if oznaka != "":
        linija_koda = 0
        while True:
            while znak < len(redovi[linija_koda]) and redovi[linija_koda][znak] != " ":
                string += redovi[linija_koda][znak]
                znak += 1

            if string == oznaka:
                znak += 1
                break
            else:
                znak = 0
                string = ""
                linija_koda += 1

        if oznaka == "KRAJ":
            break
        oznaka = ""

    string = ""
    while znak < len(redovi[linija_koda]) and redovi[linija_koda][znak] != " ":
        string += redovi[linija_koda][znak]
        znak += 1

    if string == "KRAJ" or oznaka == "KRAJ":
        break

    if string in komande:
        znak += 1
        if string == komande[0]:
            akumulator = varijable[redovi[linija_koda][znak:]]
        elif string == komande[1]:
            akumulator = int(redovi[linija_koda][znak:])
        elif string == komande[2]:
            varijable[redovi[linija_koda][znak:]] = akumulator
        elif string == komande[3]:
            akumulator += varijable[redovi[linija_koda][znak:]]
        elif string == komande[5]:
            akumulator -= varijable[redovi[linija_koda][znak:]]
        elif string == komande[6]:
            akumulator *= varijable[redovi[linija_koda][znak:]]
        elif string == komande[7]:
            akumulator /= varijable[redovi[linija_koda][znak:]]
        else:
            if akumulator < 0:
                oznaka = redovi[linija_koda][znak:]
        znak = 0
    else:
        znak += 1
        continue
    if oznaka != "":
        continue

    linija_koda += 1

    # try:
    #     string = ""
    #     if oznaka != "":
    #         while True:
    #             while znak != len(redovi[linija_koda]) and redovi[linija_koda][znak] != " ":
    #                 string += redovi[linija_koda][znak]
    #                 znak += 1
    #             if string == oznaka:
    #                 znak += 1
    #                 break
    #             else:
    #                 znak = 0
    #                 string = ""
    #                 linija_koda += 1
    #
    #         if oznaka == "KRAJ":
    #             break
    #
    #     string = ""
    #     while redovi[linija_koda][znak] != " ":
    #         string += redovi[linija_koda][znak]
    #         znak += 1
    #
    #     if string in komande:
    #         znak += 1
    #         if string == komande[0]:
    #             akumulator = varijable[redovi[linija_koda][znak:]]
    #         elif string == komande[1]:
    #             akumulator = int(redovi[linija_koda][znak:])
    #         elif string == komande[2]:
    #             varijable[redovi[linija_koda][znak:]] = akumulator
    #         elif string == komande[3]:
    #             akumulator += varijable[redovi[linija_koda][znak:]]
    #         else:
    #             if akumulator < 0:
    #                 oznaka = redovi[linija_koda][znak:]
    #         znak = 0
    #     else:
    #         znak += 1
    #         continue
    #     if oznaka != "":
    #         continue
    #
    #     linija_koda += 1
    # finally:
    #     print("Kod nije ispravno napisan.")
    #     exit(1)


print("Akumulator:", akumulator)
print(varijable)
# for key, value in varijable:
#     print(key, value, sep=": ")
izlaz = input('Pritisnite bilo koju tipku za izlaz.')
