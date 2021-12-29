## Практическая работа №6 по ВВПД.
Репозиторий содержит две основные функции, а также документацию и тесты к ним.
### Функции
* Функция `is_gray`:
```
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
```
* функция `to_gray`:
```
def to_gray(color: str) -> tuple or None:
    """
    Функция определяет - на сколько нужно изменить концентрации зеленого и синего, чтобы цвет стал серым.
    :param color: строка с цветом формата "#AAAAAA"
    :return: возвращает None, если строка не соответствует формату. tuple(int, int, int), если цвет не серый
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

    red = int(color[1:3], 16) - int(color[1:3], 16)
    green = int(color[1:3], 16) - int(color[3:5], 16)
    blue = int(color[1:3], 16) - int(color[-2:], 16)
    if red == green == blue:
        return None

    return red, green, blue
```
### Тесты
Написаны две разновидности тестов.<br/>
Одни на основе библиотеки *Pytest*, другие на 
основе *UnitTest*.
###Readme
Информация по заполнению файла readme.md была взята [отсюда](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
![picture](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1920px-Markdown-mark.svg.png)
