import math
import operator

from tapp.geometry.vector import Vector2D


class Triangle:
    """Minimal triangle interface implementation"""

    def __init__(self, a: Vector2D, b: Vector2D, c: Vector2D) -> None:
        """Validates provided sides and initializes triangle"""
        if not Triangle.is_valid(a, b, c):
            raise ValueError("Invalid triangle sides")

        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def is_valid(cls, a: Vector2D, b: Vector2D, c: Vector2D) -> bool:
        """Checks whether triangle with such sides can be constructed"""
        a_len, b_len, c_len = a.length, b.length, c.length
        if a_len != 0 and b_len != 0 and c_len != 0:
            return (
                a_len + b_len >= c_len
                and b_len + c_len >= a_len
                and c_len + a_len >= b_len
            )
        return False

    @property
    def perimeter(self) -> float:
        """Triangle perimeter"""
        return self.a.length + self.b.length + self.c.length

    @property
    def area(self) -> float:
        """Triangle area"""
        p = self.perimeter
        sides = (self.a, self.b, self.c)
        a_len, b_len, c_len = map(operator.attrgetter("length"), sides)
        return math.sqrt(p * (p - a_len) * (p - b_len) * (p - c_len))