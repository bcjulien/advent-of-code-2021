def main():
    file = open('input')

    # Reading like this to remove \n newlines from list
    lines = file.read().splitlines()

    prevLine = ""
    count = 0
    for line in lines:
        #print(line, ">", prevLine, ":", (line > prevLine))
        if line > prevLine:
            count += 1
        prevLine = line

    file.close()

    print(count)

if __name__ == "__main__":
    main()