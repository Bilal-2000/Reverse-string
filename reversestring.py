def main():
    string = input("Please enter a string: ")
    print(reverse_string(string))


def reverse_string(str):
    result = ""

    # Figuring the last index for traversal
    last_index = len(str) - 1

    # Loop to iterate over input string
    for _ in enumerate(str):
        result = result + str[last_index]
        last_index -= 1

    return result


main()
