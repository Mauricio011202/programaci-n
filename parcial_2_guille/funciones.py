def inputStr(pedido: str):
  string = input(f"Por favor ingrese un {pedido}: ")
  while not string.isalpha():
    string = input(f"Error, intente de nuevo. Por favor ingrese un {pedido}: ")
  return string

def inputInt(pedido: str):
  number = input(f"Por favor ingrese un {pedido}: ")
  while not number.isnumeric() and int(number) > 0:
    number = input(f"Error, intente de nuevo. Por favor ingrese un {pedido}: ")
  return int(number)

def inputBool(pedido: str):
  resp = input(f"Por favor ingrese 0 si es un {pedido} o 1 si no lo es: ")
  while resp not in ['0', '1']:
    resp = input(f"Error, intente de nuevo. Por favor ingrese 0 si es un {pedido} o 1 si no lo es: ")
  if (resp == '0'):
    return True
  else:
    return False
