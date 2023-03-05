import math
from copy import copy

from coordinaterow import CoordinateRow
from simplexmethods import SimplexMethods
from typing import Type

from utils import Printable, VectorUtils
from vectorbase import VectorBase, Vector2


class Simplex(SimplexMethods):
    edge_length: float = 0.5
    dimension: int = 2
    eps: float = 0.1
    start_vector: VectorBase = Vector2(1, 1)
    basis: list[VectorBase] = []
    coordinates: list[CoordinateRow] = []

    def __init__(self) -> None:
        for i in range(self.dimension + 1):
            if i == 0:
                self.basis.append(self.start_vector)
            else:
                self.basis.append(VectorBase([0] * self.dimension))
        self.coordinates.append(CoordinateRow(self.basis[0], self.get_func_value(self.basis[0])))
        self.__init_basis()

    def run(self) -> bool:
        max_index = self.__get_max()
        center = self.get_center_vector(max_index, self.dimension, self.basis)

        Printable.print_vector(center, "Центр тяжести:")
        reflected = self.get_reflected_vector(center, max_index, self.dimension, self.basis)

        Printable.print_vector(reflected, "Отраженный вектор:")
        self.coordinates.append(CoordinateRow(reflected, self.get_func_value(reflected)))

        if self.get_func_value(self.basis[max_index]) < self.get_func_value(reflected):
            min_index = self.__get_min()
            self.reduction(min_index, self.basis, self.coordinates)
        else:
            self.basis[max_index] = reflected

        center_simplex = self.get_center_simplex(self.dimension, self.basis)
        Printable.print_vector(center_simplex, "Векторное значение центра тяжести симплекса:")
        Printable.print_value(self.get_func_value(center_simplex), "Численное значение центра тяжести симплекса:")
        print("Полученный базис:")
        for i in range(len(self.basis)):
            Printable.print_vector(self.basis[i])
        return self.__is_end_of_search(self.get_func_value(center_simplex))

    def __init_basis(self) -> None:
        for i in range(1, self.dimension + 1):
            vector = self.basis[i]
            self.__init_basis_vector(vector, i)
            self.coordinates.append(CoordinateRow(copy(vector), self.get_func_value(vector)))
        print("Приращения:\n"
              f"Delta1: {VectorUtils.round_double(self.get_delta1(self.dimension, self.edge_length))}\n"
              f"Delta2: {VectorUtils.round_double(self.get_delta2(self.dimension, self.edge_length))}")
        print("Исходный базис:")
        for i in range(len(self.basis)):
            Printable.print_vector(self.basis[i])

    def __init_basis_vector(self, x: VectorBase, index: int) -> None:
        for i in range(x.dimension):
            if i + 1 == index:
                x.values[i] = self.start_vector.values[i] + self.get_delta1(self.dimension, self.edge_length)
            else:
                x.values[i] = self.start_vector.values[i] + self.get_delta2(self.dimension, self.edge_length)

    def __get_min(self) -> int:
        min_index: int = 0
        min_: float = self.get_func_value(self.basis[0])
        for i in range(len(self.basis)):
            func_value = self.get_func_value(self.basis[i])
            if func_value < min_:
                min_ = func_value
                min_index = i
        return min_index

    def __get_max(self) -> int:
        max_index: int = 0
        max_: float = self.get_func_value(self.basis[0])
        for i in range(self.dimension + 1):
            func_value = self.get_func_value(self.basis[i])
            if max_ < func_value:
                max_index = i
                max_ = func_value
        return max_index

    def __is_end_of_search(self, center_value: float) -> bool:
        for i in range(len(self.basis)):
            func_value = self.get_func_value(self.basis[i])
            if abs(func_value - center_value) > self.eps:
                return False
        return True

    def get_func_value(self, vector: VectorBase) -> float:
        return 2.8 * math.pow(vector.values[1], 2) + 1.9 * vector.values[0] + 2.7 * math.pow(vector.values[0], 2) + 1.6 - 1.9 * vector.values[1]

