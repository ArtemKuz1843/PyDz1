# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

lengthChocolate = int(input('Введите длину вашей шоколадки в дольках: '))
widthChocolate = int(input('Введите ширину вашей шоколадки в дольках: '))
sliceСhocolate = int(input('Сколько долек хотите отломить: '))

if sliceСhocolate < lengthChocolate * widthChocolate and sliceСhocolate % lengthChocolate == 0:
    print('Получится разделить шоколадку на 2 прямоугольника')
elif sliceСhocolate < lengthChocolate * widthChocolate and sliceСhocolate % widthChocolate == 0:
    print('Получится разделить шоколадку на 2 прямоугольника')
else:
    print('Не получится разделить шоколадку на 2 прямоугольника')