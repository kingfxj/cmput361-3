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
    if len(arguments) != 3:
        error("Invalid arguments")

    inputName = arguments[1]
    outputName = arguments[2]

    print(inputName, outputName)

    # Open the input json file for read
    try:
        inputFile = open(inputName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    inputData = json.load(inputFile)
    inputFile.close()
    print(inputData)

    # Open the output file for write
    try:
        outputFile = open(outputName, 'w', newline='')
    except IOError:
        error('Invalid file arguments')
    theWriter = csv.writer(outputFile, delimiter='\t')
    theWriter.writerow(['ID', 'normalized weight'])
    outputFile.close()


if __name__ == "__main__":
    main()

    print('\nDone\n')
