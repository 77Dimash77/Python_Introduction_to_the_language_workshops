# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
X = int(input('Введите трехзначное число: '))
if X > 99 and X < 1000:
  A = X // 100
  B = (X % 100) // 10
  C = X % 10
  sum= A + B + C
  print(sum)
else:
  print('Введите нормальное число')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
S = int(input('Введите общее количество журавликов'))
if S % 6 == 0:
  x = S // 6
  m1 = x
  m2 = x
  m3= 4 * x
  print(f"Петя сделал {m1} журавликов, Сережа сделал {m2} журавликов, а Катя сделала {m3} журавликов.")
else:
  print('Число не соответсвует услвоию, попробуй еще')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
S = int(input('Введите шестизначное число: '))
S = float(S)
if S > 99999 and S < 1000000:
  A = S / 1000
  A = int(A)
  B = S % 1000
  B = int(B)
  print(A, B)
  X = A // 100
  Y = (A % 100) // 10
  Z = A % 10
  sum1 = X + Y + Z
  X = B // 100
  Y = (B % 100) // 10
  Z = B % 10
  sum2 = X + Y + Z
  print(sum1, sum2)
  if sum1 == sum2:
    print('ПОВЕЗЛО')
  else:
    print('Все впереди')
else:
  print('Шестизначное Бро надо!!!')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input('Введите число высота сладкого: '))
m = int(input('Введите число ширина сладкого: '))
k = int(input('Введите число долей: '))
S = n * m
if k > S:
    result = 'no'
elif (k % n == 0) or (k % m == 0):
    result = 'yes'
else:
    result = 'no'
print(result)