from utils import VectorUtils


class VectorBase:
    def __init__(self, values: list[float]) -> None:
        self._dimension = len(values)
        self.values = values

    @property
    def values_copy(self) -> list[float]:
        return self.values.copy()

    @property
    def dimension(self) -> int:
        return self._dimension

    def __copy__(self) -> "VectorBase":
        return VectorBase(self.values)

    def __str__(self) -> str:
        result = f"Vector{self.dimension}("

        for i in range(self.dimension):
            value = "{:15f}".format(VectorUtils.round_double(self.values[i]))
            comma = ","
            if i == self.dimension - 1:
                comma = ""
            result += value + comma
        result += ")"
        return result


class Vector2(VectorBase):
    def __init__(self, x: float, y: float) -> None:
        super().__init__([x, y])
        self.x = x
        self.y = y
