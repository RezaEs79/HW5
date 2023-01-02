import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x}, y: {self.y}"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)

    def length(self):
        return math.hypot(self.x, self.y)


class Shape:
    def __init__(self) -> None:
        self.vertices = []

    def add_vertex(self, p: Point) -> None:
        self.vertices.append(p)

    def __str__(self):
        return f" number of vertices: {len(self.vertices)}"

    def perimeter(self) -> float:
        p, i = 0, 0
        if len(self.vertices) == 0:
            raise RuntimeError("No vertex")

        while i < len(self.vertices)-1:
            diff = (self.vertices[i]-self.vertices[i+1])
            p = p+math.hypot(diff.x, diff.y)
            print(f"in while: {i} , {diff.length()}")
            i = i + 1
        if len(self.vertices) > 2:
            diff = (self.vertices[i]-self.vertices[0])
            p = p+math.hypot(diff.x, diff.y)
            print(f"in while: {i} , {diff.length()}")

        return p


class Line(Shape):
    def __init__(self, p1: Point, p2: Point) -> None:
        Shape.__init__(self)
        self.add_vertex(p1)
        self.add_vertex(p2)

    def __str__(self):
        return f"line:\n\tp1:(x:{self.vertices[0].x},y:{self.vertices[0].y})\n\tp2:(x:{self.vertices[1].x},y:{self.vertices[1].y})"

    def area(self) -> float:
        return 0


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        if (p1.x == p2.x == p3.x or p1.y == p2.y == p3.y):
            raise RuntimeError("It Cann't Be Triangle")
        if (p1.x-p2.x) != 0 and (p1.x-p2.x) != 0:
            m1 = (p1.y-p2.y)/(p1.x-p2.x)
            m2 = (p2.y-p3.y)/(p2.x-p3.x)
            print(f"my check{m1}, {m2}")
            if (m1 == m2):
                raise RuntimeError("It Cann't Be Triangle")

        Shape.__init__(self)
        self.add_vertex(p1)
        self.add_vertex(p2)
        self.add_vertex(p3)

    def __str__(self):
        return f"Triangle:\n\tp1:(x:{self.vertices[0].x},y:{self.vertices[0].y})\n\tp2:(x:{self.vertices[1].x},y:{self.vertices[1].y}\n\tp3:(x:{self.vertices[2].x},y:{self.vertices[2].y})"

    def area(self) -> float:
        x1, y1 = self.vertices[0].x, self.vertices[0].y
        x2, y2 = self.vertices[1].x, self.vertices[1].y
        x3, y3 = self.vertices[2].x, self.vertices[2].y
        S = (1/2)*(x1 * (y2 - y3) + x2 * (y3 - y1) + x3*(y1 - y2))
        return abs(S)


class Rectangle(Shape):
    def __init__(self, p1: Point, p2: Point) -> None:
        if (p1.x == p2.x or p1.y == p2.y):
            raise RuntimeError("It Cann't Be Triangle")
        Shape.__init__(self)
        self.add_vertex(p1)
        self.add_vertex(p2)
        p3 = Point(p2.x, p1.y)
        p4 = Point(p1.x, p2.y)
        self.add_vertex(p3)
        self.add_vertex(p4)

    def __str__(self):
        return f"Rectangle:\n\tp1:(x:{self.vertices[0].x},y:{self.vertices[0].y})\n\tp2:(x:{self.vertices[1].x},y:{self.vertices[1].y}\n\tp3:(x:{self.vertices[2].x},y:{self.vertices[2].y}\n\tp4:(x:{self.vertices[3].x},y:{self.vertices[3].y})"

    def area(self) -> float:
        x1, y1 = self.vertices[0].x, self.vertices[0].y
        x2, y2 = self.vertices[1].x, self.vertices[1].y
        L, W = x2-x1, y2-y1
        S = abs(L*W)
        return S
