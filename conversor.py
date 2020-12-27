menu = """
  Bienvenido al conversor de monedas

  1 - Pesos colombianos
  2 - Pesos argentinos
  3 - Pesos mexicanos

  Elige una opcion:

"""

option = float(input(menu))

if option == 1:
    coin = float(input("¿Cuántos pesos colombianos tienes?"))

    dollar_value = 3500

    dollars = round(coin / dollar_value)
    dollars = str(dollars)

    print('Tienes $' + dollars + 'dólares')
elif option == 2:
    coin = float(input("¿Cuántos pesos argentinos tienes?"))

    dollar_value = 65

    dollars = round(coin / dollar_value)
    dollars = str(dollars)

    print('Tienes $' + dollars + 'dólares')
elif option == 3:
    coin = float(input("¿Cuántos pesos mexicanos tienes?"))

    dollar_value = 24

    dollars = round(coin / dollar_value)
    dollars = str(dollars)

    print('Tienes $' + dollars + 'dólares')
else:
    print('Ingresa una opción valida, por favor')
