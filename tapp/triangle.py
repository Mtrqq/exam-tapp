import math


class Triangle:
    """Minimal triangle interface implementation"""

    def __init__(self, a: float, b: float, c: float) -> None:
        """Validates provided sides and initializes triangle"""
        if not Triangle.is_valid(a, b, c):
            raise ValueError("Invalid triangle sides")

        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def is_valid(cls, a: float, b: float, c: float) -> bool:
        """Checks whether triangle with such sides can be constructed"""
        if a != 0 and b != 0 and c != 0:
            return a + b >= c and b + c >= a and c + a >= b
        return False

    @property
    def perimeter(self) -> float:
        """Triangle perimeter"""
        return self.a + self.b + self.c

    @property
    def area(self) -> float:
        """Triangle area"""
        p = self.perimeter
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
