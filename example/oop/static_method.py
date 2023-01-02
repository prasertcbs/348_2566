class LineUtil:
    @staticmethod
    def distance(c1, c2):
        # c1, c2 are list/tuple containing coordinate xy
        x1, y1 = c1
        x2, y2 = c2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

    @staticmethod
    def slope(c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        if x1 == x2:
            raise ZeroDivisionError
        return (y2 - y1) / (x2 - x1)


if __name__ == '__main__':
    c1 = (-2, -1)
    c2 = (4, 3)
    print(LineUtil.slope(c1, c2))
