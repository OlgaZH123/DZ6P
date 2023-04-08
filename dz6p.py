# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# def get_array(n, count, number):
#     array = [number]
#     while len(array) < n:
#         array.append(array[-1] + count)
#     print(*array)



# def main():
#     n = int(input('Введите размер последовательности: '))
#     count = int(input('Введите шаг последовательности: '))
#     number = int(input('Введите первый элемент последовательности: '))
#     get_array(n, count, number)


# if __name__ == '__main__':
#     main()

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_min_array_max(number_min, number_max, numbers):
    print([numbers.index(i) for i in numbers if number_min < i < number_max])


def main():
    number_min = int(input('Введите значение минимума: '))
    number_max = int(input('Введите значение максимума: '))
    numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    find_min_array_max(number_min, number_max, numbers)


if __name__ == '__main__':
    main()

