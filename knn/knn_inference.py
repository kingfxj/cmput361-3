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

    tsvName = arguments[1]
    number = int(arguments[2])
    jsonName = arguments[3]

    print(tsvName, number, jsonName)

    # Open the input json file for read
    try:
        tsvFile = open(tsvName, 'r')
    except IOError:
        error('Invalid file arguments')
    print(tsvFile)

    # Open the input json file for read
    try:
        jsonFile = open(jsonName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    jsonData = json.load(jsonFile)
    print(jsonData)


if __name__ == "__main__":
    main()

    print('\nDone\n')

#take in model -->output predictions

class KnnInference:

    def __init__(self, model, k,testCorpus):
        self.model=model
        self.k=k
        self.testCorpus=testCorpus

    def applyKnn(self):
        #for each doc?? find the nearest neighbor
        for each class get argmax 
