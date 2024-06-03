import re
def es_palindromo(palabra):
    palabra_limpia = re.sub(r'[^a-z]', '', palabra.lower())

    return palabra_limpia == palabra_limpia[::-1]
palabra = input("Introduce una palabra: ")

if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')