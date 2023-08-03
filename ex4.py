def palindromo(palavra):
    palavra = palavra.replace(' ', '').lower()
    return palavra == palavra[::-1]

print('Digite uma palavra:')
palavra = input()
print('É palíndromo:', palindromo(palavra))