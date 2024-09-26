set_countries = {'col', 'mex', 'bol'}
#tamano
size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add agregar elemento al conjunto
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)
set_countries.clear()
print(len(set_countries))


