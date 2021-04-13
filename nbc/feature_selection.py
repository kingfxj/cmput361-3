import csv, json, nltk, string, sys


def error(name):
    '''
    Print out the error and exit the program with -1
    input: name is the name of the error
    '''
    print(name, file=sys.stderr)
    exit(-1)


# Tokenize the list value
def tokenize(value):
    words = []
    for word in value:
        # Lemmatize the word
        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        word = nltk.WordNetLemmatizer().lemmatize(word)
        # Remove punctuations and make all words lower case
        words.append(word)
    return words


def main():
    # Get the arguments and validate the number of arguments
    arguments = sys.argv
    if len(arguments) != 4:
        error("Invalid arguments")

    inputName = arguments[1]
    number = int(arguments[2])
    outputName = arguments[3]

    print(inputName, number, outputName)

    # Open the input json file for read
    try:
        inputFile = open(inputName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    inputData = json.load(inputFile)
    print(inputData)


if __name__ == "__main__":
    main()

    print('\nDone\n')
