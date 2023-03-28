from vector import Vector


def main() -> None:
    test = Vector([1, 2])
    test2 = Vector([1, 2, 3])

    print(test < test2)


if __name__ == "__main__":
    main()
