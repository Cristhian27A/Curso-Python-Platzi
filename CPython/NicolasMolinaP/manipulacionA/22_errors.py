#manerajar y controlar el error
try: # para manejar con los errores en bloque
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
     raise Exception('No se permite menores de edad')
except ZeroDivisionError as error:
  print(error)
except Exception as error: 
  print(error)
except AssertionError as error:
  print(error)
  
print('Hola')