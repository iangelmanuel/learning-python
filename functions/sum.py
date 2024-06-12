def startApp():
  firtData = float(input('Ingrese el primer número: '))
  secondData = float(input('Ingrese el segundo número: '))
  print(f'La suma de los números es: {sumar(firtData, secondData)}')

def sumar (a, b):
  return a + b

startApp()