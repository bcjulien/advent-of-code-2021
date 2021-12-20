def main():
    file = open("input")
    input = file.read().splitlines()
    file.close()

    horizontal_position = 0
    depth = 0

    for line in input:
        x = line.split()
        # print(x)
        direction = x[0]
        # If isdigit returns True/False, did it just add/subtract 1's?
        # distance = x[1].isdigit()
        distance = int(x[1])

        if direction == "forward":
            horizontal_position += distance

        elif direction == "down":
            depth += distance

        elif direction == "up":
            depth -= distance

    print("Horizontal: ", horizontal_position)
    print("Depth: ", depth)
    print("Answer: ", horizontal_position * depth)


if __name__ == "__main__":
    main()