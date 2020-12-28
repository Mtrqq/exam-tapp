import math


class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None:
        if not Triangle.is_valid(a, b, c):
            raise ValueError("Invalid triangle sides")

        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def is_valid(cls, a: float, b: float, c: float) -> bool:
        if a != 0 and b != 0 and c != 0:
            return a + b >= c and b + c >= a and c + a >= b
        return False

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    @property
    def area(self) -> float:
        p = self.perimeter
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
