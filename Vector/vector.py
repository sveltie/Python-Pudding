from __future__ import annotations
import copy
import math
from typing import Any, Callable, List, Union


class Vector:
    def __init__(self, components: List[float]) -> None:
        self.components = components

    def __str__(self) -> str:
        return str(self.components)

    def __copy__(self) -> Vector:
        return Vector(self.components)

    def __deepcopy__(self, memo) -> Vector:
        return Vector(copy.deepcopy(self.components, memo))

    def __len__(self) -> int:
        return len(self.components)

    def __lt__(self, other: Vector) -> bool:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to compare")
        return self.magnitude() < other.magnitude()

    def __le__(self, other: Vector) -> bool:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to compare")
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other: Vector) -> bool:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to compare")
        return self.magnitude() > other.magnitude()

    def __ge__(self, other: Vector) -> bool:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to compare")
        return self.magnitude() >= other.magnitude()

    def __eq__(self, other: Vector) -> bool:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to compare")
        return self.magnitude() == other.magnitude()

    def __ne__(self, other: Vector) -> bool:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to compare")
        return self.magnitude != other.magnitude()

    def __getitem__(self, key) -> float:
        return self.components[key]

    def __setitem__(self, key, value) -> None:
        self.components[key] = value

    def __sub__(self, other: Vector) -> Vector:
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to subtract")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other: Union[Vector, int, float]) -> Union[float, Vector]:
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError(
                    "Vectors must be of the same dimension for multiplication"
                )
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector([a * other for a in self.components])
        else:
            raise TypeError("Multiplication is not defined for other types")

    def magnitude(self) -> float:
        return math.sqrt(sum(c**2 for c in self.components))

    def normalized(self) -> Vector:
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("Cannot normalize zero vector")
        return Vector([c / mag for c in self.components])

    def dot(self, other: Vector) -> float:
        if len(self) != len(other):
            raise ValueError(
                "Vectors must be of the same dimension to get the dot product"
            )
        return sum(a * b for a, b in zip(self.components, other.components))

    def angle(self, other: Vector) -> float:
        return math.degrees(
            math.acos((self * other) / (self.magnitude() * other.magnitude()))
        )

    # only for 2D for now
    def rotate(self, angle: float) -> Vector:
        if len(self) != 2:
            raise ValueError("Rotation is not defined for higher dimensional vector")
        angle = math.radians(angle)
        return Vector(
            [
                self[0] * math.cos(angle) + self[1] * math.sin(angle),
                -self[0] * math.sin(angle) + self[1] * math.cos(angle),
            ]
        ) # floating point error but whatever
