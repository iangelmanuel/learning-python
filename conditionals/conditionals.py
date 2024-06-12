data = int(input("Ingrese un número para saber si es par: "))

if data % 2 == 0:
  print(f"{data} el número es par")
elif data == 0:
  print(f"{data} el número es par pero es cero")
else:
  print(f"{data} el número es impar")
