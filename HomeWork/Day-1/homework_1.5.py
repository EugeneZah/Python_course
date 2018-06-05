min = int(input('Введіть кількість хвилин: '))
hours = int(min // 60)
min_clock = int(min % 60)
hours_clock = int(hours % 24)

print(hours_clock, ':', min_clock)
