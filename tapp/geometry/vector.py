import dataclasses
import math
from typing import Any


@dataclasses.dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, o: Any) -> Any:
        if not isinstance(o, Vector2D):
            return NotImplemented
        return Vector2D(
            self.x + o.x,
            self.y + o.y,
        )

    def __sub__(self, o: Any) -> Any:
        if not isinstance(o, Vector2D):
            return NotImplemented
        return Vector2D(
            self.x - o.x,
            self.y - o.y,
        )

    def __eq__(self, o: Any) -> bool:
        if not isinstance(o, Vector2D):
            return False
        return self.x == o.x and self.y == o.y

    @property
    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
