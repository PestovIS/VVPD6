def to_gray(color):
    """
    Концентрации зеленого и синего подстраиваются под концентрацию красного, чтобы концентрации были равны.
    """
    red = int(color[1:3], 16) - int(color[1:3], 16)
    green = int(color[1:3], 16) - int(color[3:5], 16)
    blue = int(color[1:3], 16) - int(color[-2:], 16)

    return red, green, blue