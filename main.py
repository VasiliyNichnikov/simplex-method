from simplex import Simplex
from utils import Printable


def main():
    simplex = Simplex()
    i = 0
    while True:
        print(f"\nИтерация: {i + 1}")
        i += 1
        if simplex.run():
            break

    Printable.print_table(simplex.coordinates)


if __name__ == '__main__':
    main()