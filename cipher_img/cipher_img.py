from PIL import Image  # Импортируем модуль Image из библиотеки Pillow для работы с изображениями
import same_size_img  # Импорт пользовательского модуля для сравнения размеров изображений
import os  # Модуль для работы с файловой системой
import random  # Импортируем модуль random для генерации случайных чисел
import string  # Импортируем модуль string для работы с набором символов и цифр

def convert(img):
    """
    Преобразует изображение в список пикселей.

    :param img: Объект изображения, поддерживающий метод getdata().
    :return: Список пикселей изображения.
    """
    return list(img.getdata())  # Возвращаем список пикселей изображения

def generate_random_message():
    """
    Генерирует случайное сообщение длиной от 5 до 20 символов.

    :return: Случайное сообщение.
    """
    length = random.randint(5, 20)  # Генерируем случайную длину от 5 до 20
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def encrypt_message(image_path, message):
    """
    Зашифровывает сообщение в изображение.

    :param image_path: Путь к изображению, в которое будет зашифровано сообщение.
    :param message: Сообщение для зашифровки.
    """
    image = Image.open(image_path)  # Открываем картинку, в которую будет зашифровано послание
    word_ascii = [ord(i) for i in message]  # Переводим послание в массив по таблице ASCII
    pixels = convert(image)  # Создание массива пикселей из картинки типа bmp
    width, height = image.size
    total_pixels = width * height

    if len(word_ascii) > total_pixels:  # Проверка на вместимость сообщения
        print("Сообщение слишком длинное для изображения!")
        return

    new_pixel_array = list(pixels)  # Массив для новой картинки с посланием

    for i in range(len(word_ascii)):
        x = i % width
        y = i // width
        new_pixel_array[y * width + x] = (0, 0, word_ascii[i])  # Зашифровываем сообщение в синий канал пикселей по порядку

    new_image = Image.new('RGB', (width, height))
    new_image.putdata(new_pixel_array)
    new_image.save('example/new_image.bmp')  # Создаем новую картинку с посланием
    new_image.show()

def decrypt_message(original_image_path, encrypted_image_path):
    """
    Дешифрует сообщение из зашифрованного изображения.

    :param original_image_path: Путь к исходному изображению.
    :param encrypted_image_path: Путь к изображению с сообщением.
    """
    if not os.path.exists(original_image_path) or not os.path.exists(encrypted_image_path):
        print("Ошибка: одно из изображений не найдено.")
        return
    original_image = Image.open(original_image_path)  # Открываем исходную картинку (это ключ для получения шифра)
    encrypted_image = Image.open(encrypted_image_path)  # Открываем картинку с посланием

    pixelsA = convert(original_image)  # переводим картинки в массив пикселей
    pixelsB = convert(encrypted_image)

    if same_size_img.compare(pixelsA, pixelsB) == False:
        print("Размеры изображений не совпадают!")
        return

    message_chars = []  # Массив для дешифрованного послания

    for pixelA, pixelB in zip(pixelsA, pixelsB):
        if pixelA != pixelB:
            message_chars.append(pixelB[2]) # Получаем послание путем вычета картинки исходной из картинки с посланием, все совпадающие пиксели отбрасываем

    message = ''.join(chr(i) for i in message_chars)  # Переводим символы ASCII
    print("Дешифрованное сообщение:", message)

while True:
    print("Выберите действие:")
    print("1. Зашифровать послание")
    print("2. Сгенерировать случайное послание и зашифровать")
    print("3. Дешифровать послание")
    choice = int(input("Введите 1, 2 или 3:"))  #Пользователь выбирает шифратор или дешифратор
    print()

    if choice == 1:
        word = input('Введите послание или RANDOM (для генерации случайно:')
        encrypt_message('example/img.bmp', word)  # Зашифровываем послание
        break

    elif choice == 2:
        random_message = generate_random_message()  # Генерируем рандомное сообщение
        print("Сгенерированное сообщение:", random_message)
        encrypt_message('example/img.bmp', random_message)
        break

    elif choice == 3:
        decrypt_message('example/img.bmp', 'example/new_image.bmp')  # Расшифровываем послание
        break

    else:
        print("\033[31mОшибка! Попробуйте снова.\033[0m")
        print()
        continue