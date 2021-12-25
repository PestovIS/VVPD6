"""
Серый цвет — множество всех цветов,получаемых путём совмещения
трёх основных цветов цветовой модели RGB — красного, зелёного и синего в равных концентрациях.
"""


def is_gray(color):
    checklist = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")

    if color[0] != '#' or len(color) != 7:
        return None
    for i in color[1:]:
        if i not in checklist:
            return None

    if color[1:3] == color[3:5] == color[-2:]:
        return True
    else:
        return False
