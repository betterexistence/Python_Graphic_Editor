# Точка
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas, size=3, color="black"):
        canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill=color, outline=color)

# Линия
class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start = start_point
        self.end = end_point

    def draw(self, canvas, color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color)

# Круг
class Circle:
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius

    def draw(self, canvas, color="blue"):
        canvas.create_oval(
            self.center.x - self.radius, self.center.y - self.radius,
            self.center.x + self.radius, self.center.y + self.radius,
            outline=color
        )

# Квадрат
class Square:
    def __init__(self, top_left: Point, size: int):
        self.top_left = top_left
        self.size = size

    def draw(self, canvas, color="green"):
        canvas.create_rectangle(
            self.top_left.x, self.top_left.y,
            self.top_left.x + self.size, self.top_left.y + self.size,
            outline=color
        )
