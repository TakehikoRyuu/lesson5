# Изменяемые и неизменяемые объекты. Кортежи 1.5
immutable_var = 1, 2, 'a', 'b'
# immutable_var[1] = v невозможно так как элемент в кортеже неизменяем
print(immutable_var)
mutable_list = [1, 2, 'a', 'b']
mutable_list[3] = 'v'
print(mutable_list)
