print("Digite um número: ")
num1 = int(input())
print("Digite outro número: ")
num2 = int(input())
print("Digite um operador: ")
operador = input()

if operador == "+":
    print("Resultado: ", num1 + num2)
elif operador == "-":
    print("Resultado: ", num1 - num2)
elif operador == "*":
    print("Resultado: ", num1 * num2)
elif operador == "/":
    print("Resultado: ", num1 / num2)
else:
    print("Operador inválido!")