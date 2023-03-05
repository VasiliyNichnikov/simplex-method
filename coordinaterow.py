from vectorbase import VectorBase


class CoordinateRow:
    def __init__(self, vector: VectorBase, func_value: float) -> None:
        self._vector = vector
        self._func_value = func_value

    @property
    def vector(self) -> VectorBase:
        return self._vector

    @property
    def func_value(self) -> float:
        return self._func_value

    def __str__(self) -> str:
        return f"{self._vector}{self._func_value}\n"

