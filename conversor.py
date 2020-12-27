coin = float(input("¿Cuántos pesos colombianos tienes?"))

dollar_value = 3500

dollars = round(coin / dollar_value)
dollars = str(dollars)

print('Tienes $' + dollars + 'dólares')
