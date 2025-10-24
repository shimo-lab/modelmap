def adjust(ax, dx, dy, dw, dh):
    pos = ax.get_position()
    new_pos = [pos.x0 + dx, pos.y0 + dy, pos.width + dw, pos.height + dh]
    ax.set_position(new_pos)

def lighter(color, amount=0.5):
    """
    Lighter color
    :param color: RGBA color
    :param amount: amount to lighten
    :return: lighter color
    """
    return tuple(min(1, c + amount) for c in color)