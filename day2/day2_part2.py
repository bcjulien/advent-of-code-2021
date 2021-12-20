def main():
    file = open("input")
    input_file = file.read().splitlines()
    file.close()

    horizontal_positon = 0
    depth = 0
    aim = 0

    for line in input_file:
        x = line.split()
        direction = x[0]
        distance = int(x[1])

        if direction == "forward":
            horizontal_positon += distance
            depth += aim * distance

        elif direction == "down":
            aim += distance

        elif direction == "up":
            aim -= distance

        """
        print(x)
        print("Horizontal: ", horizontal_positon)
        print("Depth: ", depth)
        print("Aim: ", aim)
        print("Answer: ", horizontal_positon * depth)

        input()
        """

    print("Horizontal: ", horizontal_positon)
    print("Depth: ", depth)
    print("Answer: ", horizontal_positon * depth)


if __name__ == "__main__":
    main()