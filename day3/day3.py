from os import name


def main():
    file = open("input")
    input_file = file.read().splitlines()
    file.close()

    # most common bits
    gamma = ""

    # least common bits
    epsilon = ""

    length = input_file[0].__len__()
    
    for column in range(length):
        zeros = 0
        ones = 0
        for line in input_file:
            if line[column] == '0':
                zeros += 1
            elif line[column] == '1':
                ones += 1

        
        #print(zeros, ",", ones)
        # Now make this give me the answer without doing it by hand

        if zeros < ones:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    
    print("Gamma: ", gamma)
    print("Epsilon: ", epsilon)
    print("Answer: ", binary_to_decimal(gamma), "*", binary_to_decimal(epsilon),
            "=", binary_to_decimal(gamma) * binary_to_decimal(epsilon))

# https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
def binary_to_decimal(n):
    # int(string, bytes)
    return int(n, 2)

if __name__ == "__main__":
    main()