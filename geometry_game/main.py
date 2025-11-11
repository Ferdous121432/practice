import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle) -> bool:
        # if rectangle.lowleft.x < self.x < rectangle.uptight.x and rectangle.lowleft.y < self.y < rectangle.uptight.y:
        if self.x in range(rectangle.lowleft.x, rectangle.uptight.x + 1) and \
                self.y in range(rectangle.lowleft.y, rectangle.uptight.y + 1):
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, uptight):
        self.lowleft = lowleft
        self.uptight = uptight


def main() -> bool:
    x1 = random.randint(0, 90)
    y1 = random.randint(0, 40)
    x2 = random.randint(x1+1, 100)
    y2 = random.randint(y1+1, 100)
    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    print(f"Rectangle lowleft: ({rectangle.lowleft.x}, {rectangle.lowleft.y})")
    print(f"Rectangle uptight: ({rectangle.uptight.x}, {rectangle.uptight.y})")
    user_input_x = int(input(f"Enter an x coordinate : "))
    user_input_y = int(input(f"Enter a y coordinate : "))
    point = Point(user_input_x, user_input_y)
    print(f"Point falls in rectangle: {point.falls_in_rectangle(rectangle)}")
    return point.falls_in_rectangle(rectangle)


main()
