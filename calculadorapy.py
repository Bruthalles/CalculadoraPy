def menu():
    print("*"*30)
    print(" 1 - para somar")
    print(" 2 - para subtrair")
    print(" 3 - para multiplicar")
    print(" 4 - para dividir")
    print("*"*30)

def soma(v1,v2):
    return v1+v2

def sub(v1,v2):
    return v1-v2

def mult(v1,v2):
    return v1*v2

def div(v1,v2):
    return v1/v2

while True:
    nome=input("digite (start) para começar Ou (sair) para encerrar: ")
    if nome.lower() == "sair":
        print("\n\t== Programa Encerrado ! ==")
        break
    else:    
        v1=float(input(f"digite o valor do 1º numero: "))
        v2=float(input(f"digite o valor do 2º numero: "))
        menu()

        opcao= eval(input("digite a opção desejada: "))

        if opcao ==1:
            res = soma(v1,v2)

        elif opcao ==2:
            res = sub (v1,v2)

        elif opcao ==3:
            res = mult(v1,v2)

        elif opcao ==4:
            res = div (v1,v2)

        else:
            print("opção inválida!")
            exit(0)

        print(f"o resultado da operação é {res}")


    
