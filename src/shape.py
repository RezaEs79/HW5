import math
class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x}, y: {self.y}"
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        # elif isinstance(other, tuple):
        #     return Point(self.x + other[0], self.y + other[1])
        # raise TypeError

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)

    def length(self):
        return math.hypot(self.x , self.y)

    
# p1 = Point(10, -4.5)
# p2 = Point(1, 5)
# p3=p1-p2
# p1 = Point(0, 0)
# p2 = Point(5, 0)
# p3 = Point(5, 5)
# p4 = Point(0, 5)
p1 = Point(0, 4)
p2 = Point(4, 0)
p3 = Point(4, 4)
p4 = Point(0, 0)


print(p3)
print(p3.length())


#_______________________________________


class Shape:
    def __init__(self) -> None:
        self.vertices = []

    def add_vertex(self, p:Point) -> None:
        self.vertices.append(p)

    def __str__(self):
        return f" number of vertices: {len(self.vertices)}"

    def perimeter(self) -> float:
        # for i in self.vertices:
        # p,i=0,1
        p=0
        i=0
        # print(self.vertices)

        # print(temp)
        while i < len(self.vertices)-1:
            diff=(self.vertices[i]-self.vertices[i+1])
            p=p+math.hypot(diff.x , diff.y)
            print(f"in while: {i} , {diff.length()}")
            # print(f"in while: {i} , {p}")
            i = i + 1

        return p
        # [print(i) for i in self.vertices]

rect=Shape()
rect.add_vertex(p1)
rect.add_vertex(p2)
rect.add_vertex(p3)
rect.add_vertex(p4)
print(rect)

# print(rect.perimeter())
# print("kkkkkkkkkk")
# print(math.hypot((p1-p2).x,(p1-p2).y))



class Line(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        self.p1=p1
        self.p2=p2
        # self.vertices.append(p1)

    def __str__(self):
        return f"line:\n\tp1:(x:{p1.x},y:{p1.y})\n\tp2:(x:{p2.x},y:{p2.y})"

    def area(self) -> float:
        return 0


class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point) -> None:
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def __str__(self):
        return f"Triangle:\n\tp1:(x:{p1.x},y:{p1.y})\n\tp2:(x:{p2.x},y:{p2.y}\n\tp3:(x:{p3.x},y:{p3.y})"

    def area(self) -> float:
        x1,y1=self.p1.x,self.p1.y
        x2,y2=self.p2.x,self.p2.y
        x3,y3=self.p3.x,self.p3.y
        S = (1/2)*(x1* (y2- y3 ) + x2 *(y3 -y1 ) + x3*(y1- y2))
        return abs(S)
        

class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        p3=Point(p2.x,p1.y)
        p4=Point(p1.x,p2.y)
        self.p1,self.p2,self.p3,self.p4=p1,p2,p3,p4
    def __str__(self):
        return f"Triangle:\n\tp1:(x:{p1.x},y:{p1.y})\n\tp2:(x:{p2.x},y:{p2.y}\n\tp3:(x:{p3.x},y:{p3.y}\n\tp4:(x:{p4.x},y:{p4.y})"

    def area(self) -> float:
        x1,y1=self.p1.x,self.p1.y
        x2,y2=self.p4.x,self.p4.y
        x3,y3=self.p2.x,self.p2.y
        x4,y4=self.p3.x,self.p3.y
        S=(1/2) * ((x1*y2 + x2*y3 + x3*y4 + x4*y1)-(x2*y1 + x3*y2 + x4*y3 + x1*y4))
        return S


khat=Line(p1,p2)
# print(khat.vertices.length())
sh1=Triangle(p3,p1,p2)
print(sh1.area())
sh2=Rectangle(p1,p2)
print(sh2.area())