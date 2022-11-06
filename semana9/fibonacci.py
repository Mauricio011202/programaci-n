cadena = []
def fibonacci(index, count, pre, pos):
  if index != count:
    result = pre + pos
    count += 1
    cadena.append(pos)
    fibonacci(index, count, pos, result)
  else:
    print(cadena)
