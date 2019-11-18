# https://www.geeksforgeeks.org/python-map-function/

def dobrar(n):
    return n*2

numeros = [1, 2, 3]
resultado = map(dobrar, numeros)
print(resultado)
print(list(resultado))

'''
execução:
<map object at 0x7ff0ca2d6a90>
[2, 4, 6]

'''
