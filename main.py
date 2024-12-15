import tkinter as tk
from shapes import Point, Line, Circle, Square

# Код графического редактора
class GraphicEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")
        
        self.canvas = tk.Canvas(root, bg="white", width=800, height=550)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.Y)
        
        self.points = []
        self.lines = []
        self.circles = []
        self.squares = []

        self.circle_radius = 30
        self.square_size = 60

        self.add_buttons()
        
        self.canvas.bind("<Button-1>", self.add_point)

    def add_buttons(self):
        draw_lines_button = tk.Button(self.button_frame, text="Создать линии", command=self.connect_points)
        draw_lines_button.pack(side=tk.LEFT, padx=5, pady=5)

        add_circle_button = tk.Button(self.button_frame, text="Добавить круг", command=self.add_circle)
        add_circle_button.pack(side=tk.LEFT, padx=5, pady=5)

        add_square_button = tk.Button(self.button_frame, text="Добавить квадрат", command=self.add_square)
        add_square_button.pack(side=tk.LEFT, padx=5, pady=5)

        clear_button = tk.Button(self.button_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_point(self, event):
        point = Point(event.x, event.y)
        point.draw(self.canvas)
        self.points.append(point)

    def connect_points(self):
        if len(self.points) > 1:
            for i in range(len(self.points) - 1):
                line = Line(self.points[i], self.points[i + 1])
                line.draw(self.canvas)
                self.lines.append(line)

    def add_circle(self):
        if self.points:
            center = self.points[-1]
            circle = Circle(center, self.circle_radius)
            circle.draw(self.canvas)
            self.circles.append(circle)

    def add_square(self):
        if self.points:
            top_left = self.points[-1]
            square = Square(top_left, self.square_size)
            square.draw(self.canvas)
            self.squares.append(square)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.points.clear()
        self.lines.clear()
        self.circles.clear()
        self.squares.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicEditor(root)
    root.mainloop()
