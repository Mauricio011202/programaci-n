from Employee import Developer, Accountant, HR, Employee

edificio = {
  "Desarrollo": [],
  "Contabilidad": [],
  "Recursos Humanos": []
}

ids: list [int] = []

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

def createEmployee():
  tipo = input("Ingrese:\n1 si desea crear un Desarrollador\n2 si desea crear un Contador\n3 si desea crear un Recursos Humanos\n=> ")
  while tipo not in ['1', '2', '3']:
    tipo = input("Error! Ingreso invalido. Ingrese:\n1 si desea crear un Desarrollador\n2 si desea crear un Contador\n3 si desea crear un Recursos Humanos\n=> ")
  nombre = inputStr("nombre")
  apellido = inputStr("apellido")
  cedula = inputInt("cedula")
  while cedula in ids:
    print("Esta persona ya se encuentra en el edificio")
    cedula = inputInt("cedula")
  ids.append(cedula)
  sueldo = inputInt("sueldo")
  if tipo == '1':
    lenguaje = inputStr("lenguaje de programacion")
    edificio["Desarrollo"].append(Developer(nombre, apellido, cedula, sueldo, lenguaje))
  elif tipo == '2':
    titulo = inputStr("titulo")
    edificio["Contabilidad"].append(Accountant(nombre, apellido, cedula, sueldo, titulo))
  else:
    psicologo = inputBool("psicologo")
    edificio["Recursos Humanos"].append(HR(nombre, apellido, cedula, sueldo, psicologo))

def removeEmployee(cedula: int):
  for department in edificio:
    for employee in edificio[department]:
      if employee.id in ids:
        edificio[department].remove(employee)

def printInfo(lista: list[Employee]):
  if (len(lista) > 0):
    for item in lista:
      print(f"\n----- Empleado ID:{item.id} -----")
      item.information()
      print(f"\n---------------------------------")

repeat = True
while repeat == True:
  createEmployee()
  repeat = inputBool("desea repetir")

for department in edificio:
  print(f"\nDepartamento: {department}")
  printInfo(edificio[department])

print("\n\nSalida del empleado")
remove = inputInt("cedula")
while remove not in ids:
  print("Esta persona no esta en el edificio")
  print(ids)
  remove = inputInt("cedula")
removeEmployee(remove)

for department in edificio:
  print(f"\nDepartamento: {department}")
  printInfo(edificio[department])





