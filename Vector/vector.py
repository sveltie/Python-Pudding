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
        """Calculate the magnitude or the length of a vector

        Parameters
        ----------
        Self@Vector

        Returns
        -------
        float
            Magnitude of a given vector

        Examples
        --------
        >>> a = Vector([1, 2, 3])
        >>> a.magnitude()
        """

        return math.sqrt(sum(c**2 for c in self.components))

    def normalized(self) -> Vector:
        """Normalize a vector

        A normalized vector is calculated by dividing each component of the vector by
        it's magnitude or length

        Parameters
        ----------
        Self@Vector

        Returns
        -------
        Vector
            A normalized vector

        Raises
        ------
        ZeroDivisionError
            if vector magnitude or length is zero a.k.a zero vector

        Examples
        --------
        >>> a = Vector([1, 2, 3])
        >>> a.normalized()
        """

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

    # only for 2D and 3D for now
    def rotate(self, angle: float, axis=Union[None, str]) -> Vector:
        angle = math.radians(angle)
        if len(self) == 2:
            x, y = self
            return Vector(
                [
                    round(x * math.cos(angle) - y * math.sin(angle)),
                    round(x * math.sin(angle) + y * math.cos(angle)),
                ]
            )  # floating point error but whatever
        elif len(self) == 3:
            x, y, z = self
            if axis is None:
                raise TypeError("Axis were not provided")
            elif axis == "x":
                return Vector(
                    [
                        x,
                        round(y * math.cos(angle) - z * math.sin(angle)),
                        round(y * math.sin(angle) + z * math.cos(angle)),
                    ]
                )
            elif axis == "y":
                return Vector(
                    [
                        round(x * math.cos(angle) + z * math.sin(angle)),
                        y,
                        round(-x * math.sin(angle) + z * math.cos(angle)),
                    ]
                )
            elif axis == "z":
                return Vector(
                    [
                        round(x * math.cos(angle) - y * math.sin(angle)),
                        round(x * math.sin(angle) + y * math.cos(angle)),
                        z,
                    ]
                )
            else:
                raise ValueError(f"Rotation on axis {axis} is not defined")
        else:
            raise TypeError(
                "Rotation is not defined for higher dimension yet or other types"
            )
