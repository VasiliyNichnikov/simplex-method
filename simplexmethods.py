import math
from abc import ABC, abstractmethod

from coordinaterow import CoordinateRow
from utils import Printable
from vectorbase import VectorBase


class SimplexMethods(ABC):
    @staticmethod
    def get_center_vector(index: int, dimension: int, basis: list[VectorBase]) -> VectorBase:
        center = VectorBase([0] * dimension)
        for i in range(len(basis)):
            if i == index:
                continue

            for j in range(dimension):
                center.values[j] += basis[i].values[j]

        for j in range(dimension):
            center.values[j] /= dimension
        return center

    @staticmethod
    def get_reflected_vector(center: VectorBase, index: int, dimension: int, basis: list[VectorBase]) -> VectorBase:
        reflected_vector = VectorBase([0] * dimension)
        for i in range(dimension):
            reflected_vector.values[i] = 2 * center.values[i] - basis[index].values[i]
        return reflected_vector

    @staticmethod
    def get_center_simplex(dimension: int, basis: list[VectorBase]) -> VectorBase:
        center = VectorBase([0] * dimension)
        for i in range(len(basis)):
            for j in range(dimension):
                center.values[j] += basis[i].values[j]

        for i in range(dimension):
            center.values[i] /= dimension + 1
        return center

    @staticmethod
    def get_delta1(dimension: int, edge_length: float) -> float:
        return (math.sqrt(dimension + 1) - 1) / (dimension * math.sqrt(2)) * edge_length

    @staticmethod
    def get_delta2(dimension: int, edge_length: float) -> float:
        return (math.sqrt(dimension + 1) + dimension - 1) / (dimension * math.sqrt(2)) * edge_length

    def reduction(self, min_index: int, basis: list[VectorBase], coordinates: list[CoordinateRow]) -> None:
        for i in range(len(basis)):
            if i == min_index:
                continue

            for j in range(len(basis) - 1):
                basis[i].values[j] = basis[min_index].values[j] + 0.5 * (basis[i].values[j] - basis[min_index].values[j])

            vector = basis[i]
            func_value = self.get_func_value(basis[i])

            Printable.print_vector(vector, "Редуцированный вектор:")
            Printable.print_value(func_value, "Численное значение:")
            coordinates.append(CoordinateRow(vector, func_value))

    @abstractmethod
    def get_func_value(self, vector: VectorBase) -> float:
        pass
