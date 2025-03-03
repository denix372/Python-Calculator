def adunare(x, y):
    return x + y

def scadere(x, y):
    return x - y

def inmultire(x, y):
    return x * y

def impartire(x, y):
    if y == 0:
        return "Eroare! Nu se poate imparti la 0."
    else:
        return x / y
        
def calculator():
    print("Alegeti operatia dorita:")
    print("1. Adunare")
    print("2. Scadere")
    print("3. Inmultire")
    print("4. Impartire")

    alegere = input("Introduceti opriunea (1/2/3/4): ")

    if alegere in ['1', '2', '3', '4']:
        num1 = float(input("Introduceri primul numar: "))
        num2 = float(input("Introduceri al doilea numar: "))

        if alegere == '1':
            print(f"{num1} + {num2} = {adunare(num1, num2)}")
        elif alegere == '2':
            print(f"{num1} - {num2} = {scadere(num1, num2)}")
        elif alegere == '3':
            print(f"{num1} * {num2} = {inmultire(num1, num2)}")
        elif alegere == '4':
            print(f"{num1} / {num2} = {impartire(num1, num2)}")
    else:
        print("Optiune invalida")

calculator()
