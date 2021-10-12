Soma = lambda x,y : x+y
Sub = lambda x,y : x-y
Mult = lambda x,y : x*y
Div = lambda x,y : x/y

enunciado = """
Selecione o número da operação desejada:

1 - Soma
2 - Subtração 
3 - Multiplicação
4 - Divisão

"""

print(enunciado)

opera = int(input("Informe o número relativo à operação desejada \n\n\n"))

n1 = int(input("Primeiro numero:\n"))

n2 = int(input("Segundo numero:\n"))


if opera == 1:
    print(Soma(n1,n2))
elif opera == 2:
    print(Sub(n1,n2))
elif opera == 3:
    print(Mult(n1,n2))
elif opera == 4:
    print(Div(n1,n2))
elif opera >= 5:
    print("Operação inválida. Inicie o programa novamente.")    