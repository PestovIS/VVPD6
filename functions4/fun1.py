
def is_gray(color: str) -> bool or None:
    """
    Функция определяет - является ли вводимый цвет серым.
    :param color: строка с цветом формата "#AAAAAA"
    :return: возвращает None, если строка не соответствует формату. False, если цвет не серый. True, если цвет серый.
    """
    checklist = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    if type(color) is str:
        if color[0] != '#' or len(color) != 7:
            return None
        for i in color[1:]:
            if i not in checklist:
                return None
    else:
        return None

    if color[1:3] == color[3:5] == color[-2:]:
        return True
    else:
        return False


is_gray(0)
is_gray('#111111')
is_gray('#111110')
is_gray('asdf')
is_gray('#11111N')
