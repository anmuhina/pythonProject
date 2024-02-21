import math

# проверка образует три точки поворот против(>0) часовой стрелки или по(<0)
def criterion_of_orientatation(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

def intersect(A, B, C, D):
    return (criterion_of_orientatation(A, C, D) != criterion_of_orientatation(B, C, D)
            and criterion_of_orientatation(A, B, C) != criterion_of_orientatation(A, B, D))

def is_point_inside_polygon(point, polygon):
    def sign(p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    n = len(polygon)
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        if (a.y <= point.y < b.y or b.y <= point.y < a.y) and point.x < a.x + (b.x - a.x) * (p.y - a.y) / (b.y - a.y):
            return True
        else:
            return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def movePoint(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod
    def dist(p2, p1):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


class Figure:
    def __init__(self, identifier):
        self.identifier = identifier

    def move(self, dx, dy):
        pass

    def area(self):
        pass

    @staticmethod
    def compare(one_shape, other_shape):
        area1 = one_shape.area()
        area2 = other_shape.area()
        if area1 > area2:
            return f"{one_shape.identifier} имеет большую площадь."
        elif area1 < area2:
            return f"{other_shape.identifier} имеет большую площадь."
        else:
            return "Площади данных фигур равны."


class Triangle(Figure):
    def __init__(self, identifier, a, b, c):
        super().__init__(identifier)
        self.A = a
        self.B = b
        self.C = c
        self.ab = Point.dist(self.A, self.B)
        self.ac = Point.dist(self.A, self.C)
        self.bc = Point.dist(self.B, self.C)
        if self.ab >= self.bc + self.ac or self.ac >= self.bc + self.ab or self.bc >= self.ab + self.ac:
            raise Exception(self.identifier + " is not a triangle!\n")

    def area(self):
        p = (self.ab + self.ac + self.bc) / 2
        return math.sqrt(p * (p - self.ab) * (p - self.ac) * (p - self.bc))

    def move(self, dx, dy):
        self.A.movePoint(dx, dy)
        self.B.movePoint(dx, dy)
        self.C.movePoint(dx, dy)

    '''def is_point_inside(self, point):
        # Функция для проверки, находится ли точка внутри треугольника
        def sign(A, B, C):
            return (A.x - C.x) * (B.y - C.y) - (B.x - C.x) * (A.y - C.y)
        b1 = sign(point, self.A, self.B) < 0.0
        b2 = sign(point, self.B, self.C) < 0.0
        b3 = sign(point, self.C, self.A) < 0.0
        return ((b1 == b2) and (b2 == b3))

    def is_include(self, A, B, C, D, E):
        if self.is_point_inside(A) == 1 and self.is_point_inside(B) ==1 and self.is_point_inside(C) == 1 and self.is_point_inside(D) == 1 and self.is_point_inside(E) == 1:
            return True
        else:
            return False'''

    def is_intersect(self, other_triangle):
        if not isinstance(other_triangle, Triangle):
            raise TypeError("One of the figures is not a triangle!")
        points1 = [self.A, self.B, self.C]
        points2 = [other_triangle.A, other_triangle.B, other_triangle.C]
        for i in range(0, 3):
            for j in range(0, 3):
                if i + 1 == 3:
                    k = 0
                else:
                    k = i + 1
                if 1 + j == 3:
                    l = 0
                else:
                    l = j + 1
                if intersect(points1[i], points1[k], points2[j], points2[l]):
                    return True
        return False

    def print_coordinates_of_triangle(self):
        return ("Coordinates of " + self.identifier + ": (" + str(self.A.x) + "," +
                str(self.A.y) + "), (" + str(self.B.x) + "," + str(self.B.y) + "), (" +
                str(self.C.x) + "," + str(self.C.y) + ")")


class Pentagon(Figure):
    def __init__(self, identifier, a, b, c, d, e):
        super().__init__(identifier)
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.E = e
        self.ab = Point.dist(self.A, self.B)
        self.bc = Point.dist(self.B, self.C)
        self.cd = Point.dist(self.C, self.D)
        self.de = Point.dist(self.D, self.E)
        self.ea = Point.dist(self.E, self.A)

    def area(self):
        p = (self.ab + self.bc + self.cd + self.de + self.ea) / 2
        return math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.cd) * (p - self.de) * (p - self.ea))

    def move(self, dx, dy):
        self.A.movePoint(dx, dy)
        self.B.movePoint(dx, dy)
        self.C.movePoint(dx, dy)
        self.D.movePoint(dx, dy)
        self.E.movePoint(dx, dy)

    def is_intersect(self, other_pentagon):
        points1 = [self.A, self.B, self.C, self.D, self.E]
        points2 = [other_pentagon.A, other_pentagon.B, other_pentagon.C, other_pentagon.D, other_pentagon.E]

        for i in range(5):
            for j in range(5):
                if i + 1 == 5:
                    k = 0
                else:
                    k = i + 1
                if 1 + j == 5:
                    l = 0
                else:
                    l = j + 1
                if intersect(points1[i], points1[k], points2[j], points2[l]):
                    return True
        return False

    def print_coordinates_of_pentagon(self):
        return ("Coordinates of " + self.identifier + ": (" + str(self.A.x) + "," + str(self.A.y) + "), (" +
                str(self.B.x) + "," + str(self.B.y) + "), (" + str(self.C.x) + "," + str(self.C.y) + "), (" +
                str(self.D.x) + "," + str(self.D.y) + "), (" + str(self.E.x) + "," + str(self.E.y) + ")")


# треугольники
try:
    point1 = Point(6, 5)
    point2 = Point(9, 5)
    point3 = Point(9, 8)
    t1 = Triangle("triangle1", point1, point2, point3)

    point4 = Point(7, 9)
    point5 = Point(9, 3)
    point6 = Point(11, 7)
    t2 = Triangle("triangle2", point4, point5, point6)

    point7 = Point(0, 0)
    point8 = Point(1, 1)
    point9 = Point(7, 7)
    #t3 = Triangle("triangle3", point7, point8, point9)

    print(t1.print_coordinates_of_triangle())
    print(t2.print_coordinates_of_triangle() + "\n")

    if t1.is_intersect(t2) == True:
       print("Triangles are intersected\n")
    else:
       print("Triangles aren't intersected\n")

    t1.move(1, 1)
    print("New " + t1.print_coordinates_of_triangle())
    t2.move(3, -1)
    print("New " + t2.print_coordinates_of_triangle() + "\n\n")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

# пятиугольники
p1 = Point(3, 4)
p2 = Point(9, 1)
p3 = Point(13, 5)
p4 = Point(8, 10)
p5 = Point(3, 8)
pen1 = Pentagon("pentagon1", p1, p2, p3, p4, p5)

p6 = Point(1, 13)
p7 = Point(3, 11)
p8 = Point(5, 12)
p9 = Point(6, 14)
p10 = Point(2, 14)
pen2 = Pentagon("pentagon2", p6, p7, p8, p9, p10)

print(pen1.print_coordinates_of_pentagon())
print(pen2.print_coordinates_of_pentagon() + "\n")

if pen1.is_intersect(pen2) == True:
    print("Pentagons are intersected\n")
else:
    print("Pentagons aren't intersected\n")

pen1.move(1, 1)
print("New " + pen1.print_coordinates_of_pentagon())
pen2.move(3, -1)
print("New " + pen2.print_coordinates_of_pentagon())
