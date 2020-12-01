def verificar_repeticao(numero):
    if numero < 10:
        return True
    if 10 <= numero < 100:
        d1 = numero // 10
        d2 = numero - d1 * 10
        if d1 == d2:
            return False
        else:
            return True
    if 100 <= numero < 1000:
        d1 = numero // 100
        d2 = (numero - d1 * 100) // 10
        d3 = numero - (d1 * 100 + d2 * 10)
        if d1 == d2 or d1 == d3 or d2 == d3:
            return False
        else:
            return True
    if numero >= 1000:
        d1 = numero // 1000
        d2 = (numero - d1 * 1000) // 100
        d3 = (numero - (d1 * 1000 + d2 *100)) // 10
        d4 = numero - (d1 * 1000 + d2 * 100 + d3 * 10)
        if d1 == d2 or d1 == d3 or d1 == d4 or d2 == d3 or d2 == d4 or d3 == d4:
            return False
        else:
            return True

n1 = int(input())
n2 = int(input())
possiveis = 0

while n1 <= n2:
    if verificar_repeticao(n1):
        possiveis += 1
    n1 += 1

print(possiveis)
