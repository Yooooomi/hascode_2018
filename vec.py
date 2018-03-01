def calc_dist(vec1, vec2):
    return abs(vec1.x - vec2.x) + abs(vec1.y - vec2.y)


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y