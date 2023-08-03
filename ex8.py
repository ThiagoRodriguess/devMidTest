def interest_calculator(amount, rate, time):
    return amount * (1 + rate/100) ** time

print("Digite o valor inicial:")
amount = float(input())
print("Digite a taxa de juros:")
rate = float(input())
print("Digite o tempo de aplicação:")
time = int(input())

print("Valor final:", interest_calculator(amount, rate, time))