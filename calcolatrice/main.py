def somma(op1, op2):
    r=op1+op2
    return r

def sottrazione(op1, op2):
    r=op1-op2
    return r

def moltiplicazione(op1, op2):
    r=op1*op2
    return r

def divisione(op1, op2):
    r=op1/op2
    return r

x=0
while x!=10:
    print("primo operando")
    a=float(input())

    print("operatore")
    o=input()

    print("secondo operatore")
    b=float(input())

    match o:
        case "+":
            ris=somma(a, b)
            print("il risultato è: "+ str(ris))

        case "-":
            ris=sottrazione(a, b)
            print("il risultato è: "+ str(ris))

        case "*":
            ris=moltiplicazione(a, b)
            print("il risultato è: "+ str(ris))

        case "/":
            ris=divisione(a, b)
            print("il risultato è: "+ str(ris))

        case _:
            print("errore di inserimento")
x+1