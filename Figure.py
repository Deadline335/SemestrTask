import turtle, math
t = turtle 

class Circle:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

        if self.d <= 0:
            raise ValueError("Error")
    
    def get_area(self):
        return math.pi * (self.d/2)**2

    def get_perimetr(self):
        return 2 * math.pi * (self.d/2)

    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        t.circle(self.d/2)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()

class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        if self.size <= 0:
            raise ValueError("Error")

    def get_area(self):
        return self.size ** 2

    def get_perimetr(self):
        return 4 * self.size
    
    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        for i in range(4):
            t.forward(self.size)
            t.left(90)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()

class Rectangle:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_y = size_y
        self.size_x = size_x 
        if self.size_y <= 0 or self.size_x <= 0:
            raise ValueError("Error")

    def get_area(self):
        return self.size_x * self.size_y 

    def get_perimetr(self):
        return 2*(self.size_x + self.size_y)

    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        for i in range(4):
            t.forward(self.size_x) if i % 2 == 0 else t.forward(self.size_y)
            t.left(90)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()

class Triangle: 
    def __init__(self, x, y, size_a, size_b, angle):
        self.x = x 
        self.y = y 
        self.size_a = size_a 
        self.size_b = size_b
        self.angle = angle

        if self.size_a <= 0 or self.size_b <= 0 or self.angle <= 0 or self.angle > 179:
            raise ValueError("Error")

        self.__size_c = math.sqrt(self.size_a ** 2 + self.size_b ** 2 - 2 * self.size_a * self.size_b * math.cos(math.radians(self.angle)))
        self.__angels = 180 - math.degrees(math.acos((self.size_b ** 2 + self.__size_c ** 2 - self.size_a ** 2) / (2 * self.size_b * self.__size_c)))

    def get_area(self):
        return 0.5 * self.size_a * self.size_b * math.sin(math.radians(self.angle))
    
    def get_perimetr(self):
        return self.size_a + self.size_b + self.__size_c

    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        t.forward(self.size_a)
        t.left(180 - self.angle)
        t.forward(self.size_b)
        t.left(self.__angels)
        t.forward(self.__size_c)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()

class Pentagon:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

        if self.side <= 0:
            raise ValueError("Error")

        self.__angels = 360 / 5
    
    def get_area(self):
        return ((self.side ** 2) * 5) / (4 * (math.tan(math.pi / 5)))

    def get_perimetr(self):
        return self.side * 5

    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        for i in range(5):
            t.forward(self.side)
            t.left(self.__angels)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()

class Hexagon:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    
        if self.side <= 0:
            raise ValueError("Error")

        self.__angels = 360 / 6
    
    def get_area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2
    
    def get_perimetr(self):
        return self.side * 6
    
    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        for i in range(6):
            t.forward(self.side)
            t.left(self.__angels)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()

class Ellipse:
    def __init__(self, x, y, r1, r2):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
    
        if self.r1 <= 0 or self.r2 <= 0:
            raise ValueError("Error")

    def get_area(self):
        return math.pi * self.r1 * self.r2
    
    def get_perimetr(self):
        self.__h = ((self.r1 - self.r2) / (self.r1 + self.r2)) ** 2
        return math.pi * (self.r1 + self.r2) * (1 + (3 * self.__h) / (10 + math.sqrt(4 - 3 * self.__h)))
    def drawing_figure(self, line_color, fill_color):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(line_color, fill_color)
        t.begin_fill()
        t.circle(self.r1, 45)
        t.circle(self.r2, 90)
        t.circle(self.r1, 90)
        t.circle(self.r2, 90)
        t.circle(self.r1, 45)
        t.end_fill()
        t.pu()
        t.home()
        t.pd()





            
             

    

