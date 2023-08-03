def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print('Digite um número inteiro positivo:')
n = int(input())
print("Seu fatorial é:", fatorial(n))