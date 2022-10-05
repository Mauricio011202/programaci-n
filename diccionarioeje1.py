
currency_dict= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currenc_input= input("Plese enter a currency, eg: Euro, Dollar or Yen")
print(currency_dict.get(currency_dict.title(), "Currency not Found"))

