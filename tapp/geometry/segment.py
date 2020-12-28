from tapp.geometry.vector import Vector2D


class Segment:
    def __init__(self, a: Vector2D, b: Vector2D) -> None:
        if not Segment.is_valid(a, b):
            raise ValueError("Equal segment points detected")

        self.a = a
        self.b = b

    @classmethod
    def is_valid(cls, a: Vector2D, b: Vector2D) -> bool:
        return a != b

    @property
    def length(self) -> float:
        return (self.b - self.a).length
