def n_vogais(texto):
    texto = texto.lower()
    vogais = 'aeiouáéíóúâêôãõ'
    return sum([texto.count(vogal) for vogal in vogais])

print('Digite um texto:')
texto = input()
print('Número de vogais:', n_vogais(texto))