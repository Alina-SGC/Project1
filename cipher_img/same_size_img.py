def compare (pixelsA, pixelsB):
    """
    Сравнивает два списка пикселей (pixelsA и pixelsB) на равенство их размерности.

    Аргументы:
    pixelsA: Список пикселей первого изображения.
    pixelsB: Список пикселей второго изображения.

    Возвращает:
    bool: True, если списки имеют одинаковую длину;
           False в противном случае. Если длины различаются,
           выводит сообщение об ошибке.
    """
    if len(pixelsA) != len(pixelsB):  # Для правильной дешифровки, сообщения должны быть одинаковой размерности
        print("\033[31mИзображения разного рамера\033[0m")
    return len(pixelsA) == len(pixelsB)