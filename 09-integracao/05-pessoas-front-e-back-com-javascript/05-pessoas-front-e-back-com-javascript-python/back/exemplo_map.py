# https://www.geeksforgeeks.org/python-map-function/

def dobrar(n):
    return n*2

numeros = [1, 2, 3]
resultado = map(dobrar, numeros)
print(resultado)
print(list(resultado))