def to_gray(color):
    """
    Концентрации зеленого и синего подстраиваются под концентрацию красного, чтобы концентрации были равны.
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


to_gray(1243)
to_gray('#FFFFFF')
to_gray('FFFFFF')
to_gray('#FFFFFM')
to_gray('#F88954')

