#Create a program that receives a number from the user and displays the table of that number, from 1 to 10.

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print("Digite um número inteiro:")
n = int(input())
tabuada(n)
