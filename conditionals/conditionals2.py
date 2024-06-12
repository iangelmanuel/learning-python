n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese un tercer número: "))

if n1 > n2 and n1 > n3:
  print(f"El número {n1} es el mayor")
elif n2 > n1 and n2 > n3:
  print(f"El número {n2} es el mayor")
else:
  print(f"El número {n3} es el mayor")
