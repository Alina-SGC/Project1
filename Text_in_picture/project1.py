import numpy as np
from PIL import Image

while True:
    print("Выберите действие:")
    print("1. Зашифровать послание")
    print("2. Дешифровать послание")
    choice = int(input("Введите 1 или 2:")) #Пользователь выбирает шифратор или дешифратор
    print()

    if choice == 1:
        image = Image.open('img.bmp') #Открываем картинку, в которую будет зашифровано послание
        word = input('Введите послание:')
        word_ascii = [ord(i) for i in word] #Переводим послание в массив по таблице ASCII
        pixels = list(image.getdata()) #Создание массива пикселей из картинки типа bmp
        width, height = image.size
        total_pixels = width * height

        if len(word_ascii) > total_pixels: #Проверка на вместимость сообщения
            print("Сообщение слишком длинное для изображения!")
            break

        new_pixel_array = list(pixels) #Массив для новой картинки с посланием

        for i in range(len(word_ascii)):
            x = i % width
            y = i // width
            new_pixel_array[y * width + x] = (0, 0, word_ascii[i]) #Зашифровываем сообщение в синий канал пикселей по порядку

        new_image = Image.new('RGB', (width, height))
        new_image.putdata(new_pixel_array)
        new_image.save('new_image.bmp') #Создаем новую картинку с посланием
        new_image.show()

        break

    elif choice == 2:
        image = Image.open('img.bmp')  #Открываем исходную картинку (это ключ для получения шифра)
        new_image = Image.open('new_image.bmp')  #Открываем картинку с посланием

        pixelsA = list(image.getdata()) #переводим картинки в массив пикселей
        pixelsB = list(new_image.getdata())

        if len(pixelsA) != len(pixelsB): #Для правильной дешифровки, сообщения должны быть одинаковой размерности
            print("\033[31mИзображения разного рамера\033[0m")
            break

        message_chars = [] #Массив для дешифрованного послания

        for pixelA, pixelB in zip(pixelsA, pixelsB):
            if pixelA != pixelB:
                message_chars.append(pixelB[2])  #Получаем послание путем вычета картинки исходной из картинки с посланием, все совпадающие пиксели отбрасываем

        message = ''.join(chr(i) for i in message_chars )  # Переводим символы ASCII
        print("Дешифрованное сообщение:", message)
        break

    else:
        print("\033[31mОшибка! Попробуйте снова.\033[0m")
        print()
        continue