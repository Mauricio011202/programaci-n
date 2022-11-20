def inputStr(pedido: str):
  string = input(f"Por favor ingrese un {pedido}: ")

  return string

def inputInt(pedido: str):
  number = input(f"Por favor ingrese un {pedido}: ")
  while not number.isnumeric() and int(number) > 0:
    number = input(f"Error, intente de nuevo. Por favor ingrese un {pedido}: ")
  return int(number)