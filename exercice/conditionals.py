capital = 2000

print('1. Ingresar dinero')
print('2. Retirar dinero')
print('3. Mostrar dinero')
print('4. Salir')

option = int(input('Ingrese la acción que desea realizar: '))

if option == 1:
    amount = int(input('Ingrese la cantidad de dinero que desea ingresar: '))
    capital += amount
    print(f'Su saldo actual es de {capital}')
elif option == 2:
    amount = int(input('Ingrese la cantidad de dinero que desea retirar: '))
    if amount > capital:
        print('No puede retirar más dinero del que tiene en su cuenta')
    else:
        capital -= amount
        print(f'Su saldo actual es de {capital}')

elif option == 3:
    print(f'Su saldo actual es de {capital}')
elif option == 4:
    print('Gracias por usar nuestros servicios')
else:
    print('Opción inválida')
  