line_1 = ('*' * 20)
len_line_1 = len(line_1)
name = input('Введіть своє імя: ')
len_name = len(name)
rem = int((len_line_1 - len_name) / 2 - 1)
line_2 = '*' + (' ' * rem) + name + (' ' * rem) + '*'

print(line_1)
print(line_2)
print(line_1)
