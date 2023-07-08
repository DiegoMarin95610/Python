#potencias de 2 hasta el numero mil
from unittest import result


def run():
    LIMIT = 1000
    count = 2

    while count <= LIMIT:
        print("2 elevado a la " + str(count))
        count += 2


if __name__ == '__main__':
    run()