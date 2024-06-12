name1 = input("Ingrese un nombre: ")
name2 = input("Ingrese otro nombre: ")

if name1[0] == name2[0] or name1[-1] == name2[-1]:
  print("Los nombres empiezan o terminan con la misma letra")
else:
  print("Los nombres no empiezan o terminan con la misma letra")
