stroka = 'firefly'
if stroka.count('f') == 0:  # Если в строке нет 'f':
    None                    # то ничего не делать
elif stroka.count('f') > 1:   # А если 'f' в строке больше 1го:
    print(stroka.find('f'))  # Метод find() показывает индекс первого 'f' в строке
    print(stroka.rfind('f'))  # Метод rfind() показывает индекс последнего 'f' в строке
else:                         # Иначе
    print(stroka.find('f'))  # Метод find() показывает индекс первого 'f' в строке

