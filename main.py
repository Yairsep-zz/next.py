import functools

input_file = open("./files/names.txt", "r")
word_Split = input_file.read().split("\n")


# numOfWords = len(word_Split)
def createNameLengthFile():
    file = open("files/name_length.txt", "w")
    for word in word_Split: file.write(str(len(word)) + "\n")
    file.close()


def printNamesByInputName():
    number = input("Enter name length:")
    for word in word_Split:
        if len(word) == int(number):
            print(word)


def main():
    # Chapter 1
    print(word_Split)
    print(max(word_Split, key=len))
    print(sum(len(word) for word in word_Split))
    createNameLengthFile()
    printNamesByInputName()

    # Chapter 2


if __name__ == "__main__":
    main()
