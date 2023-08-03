def primo(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


primos = []

for i in range(1, 100):
    if primo(i):
        primos.append(i)
    if len(primos) == 10:
        break

print("Os 10 primeiros números primos são:")
print(*primos, sep=", ")
