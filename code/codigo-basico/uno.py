print('ingresar el primer numero')
numero1 = int(input())
print('Ingresar el segundo número')
numero2 = int(input())
if numero1<numero2:
    print('número menor es el:',numero1)
    f = open('holamundo.txt','a')
    f.write('\n' + 'Hola Mundo')
    f.close()
else:
    print('el número menor es el:',numero2)