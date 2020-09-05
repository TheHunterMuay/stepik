a = input()
b = input()
if (a =='красный' and b == 'синий') or (a =='синий' and b == 'красный'):
    print('фиолетовый')
elif (a =='красный' and b == 'желтый') or (a =='желтый' and b == 'красный'):
    print('оранжевый')
elif (a =='синий' and b == 'желтый') or (a =='желтый' and b == 'синий'):
    print('зеленый')
elif a==b and (a =='красный' or a == 'синий' or a =='желтый'):
    print(a)
else:
    print('ошибка цвета')