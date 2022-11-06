from Employee import Developer, Accountant, HR, Employee

edificio = {
  "Desarrollo": [],
  "Contabilidad": [],
  "Recursos Humanos": []
}

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

def createDev():
  nombre = inputStr("nombre")
  apellido = inputStr("apellido")
  cedula = inputInt("cedula")
  sueldo = inputInt("sueldo")
  lenguaje = inputStr("lenguaje de programacion")
  edificio["Desarrollo"].append(Developer(nombre, apellido, cedula, sueldo, lenguaje))

def createAcc():
  nombre = inputStr("nombre")
  apellido = inputStr("apellido")
  cedula = inputInt("cedula")
  sueldo = inputInt("sueldo")
  titulo = inputStr("titulo")
  edificio["Contabilidad"].append(Accountant(nombre, apellido, cedula, sueldo, titulo))

def createHR():
  nombre = inputStr("nombre")
  apellido = inputStr("apellido")
  cedula = inputInt("cedula")
  sueldo = inputInt("sueldo")
  psicologo = inputBool("psicologo")
  edificio["Recursos Humanos"].append(HR(nombre, apellido, cedula, sueldo, psicologo))

def printInfo(lista: list[Employee]):
  for item in lista:
    item.information()

createDev()
createAcc()
createHR()

for department in edificio:
  print(f"Departamento: {department}")
  printInfo(edificio[department])






