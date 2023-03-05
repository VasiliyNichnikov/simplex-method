class Printable:
    @staticmethod
    def print_vector(vector: "VectorBase", message: None | str = None) -> None:
        if message is not None:
            print(message)
        print(vector)

    @staticmethod
    def print_value(value: float, message: None | str = None) -> None:
        if message is not None:
            print(message)
        print(VectorUtils.round_double(value))

    @staticmethod
    def print_table(coordinates: list["CoordinateRow"]) -> None:
        print()
        print("Таблица векторов: ")
        for row in coordinates:
            vector = row.vector
            print(f"{vector}. Func value: {'{:15f}'.format(VectorUtils.round_double(row.func_value))}", end="\n")


class VectorUtils:
    @staticmethod
    def is_equal(vector1: "VectorBase", vector2: "VectorBase") -> bool:
        if vector1.dimension != vector2.dimension:
            return False
        for i in range(vector1.dimension):
            if vector1.values[i] != vector2.values[i]:
                return False
        return True

    @staticmethod
    def round_double(value: float) -> float:
        return round(value * 1000) / 1000
