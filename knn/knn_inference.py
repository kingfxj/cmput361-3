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

# Take in model -->output predictions

class KnnInference:

    def __init__(self, model, k, testCorpus):
        self.model=model
        self.k=k
        self.testCorpus=testCorpus

    def applyKnn(self):
        # For each doc?? find the nearest neighbor
        # for each class get argmax 
        pass


def main():
    # Get the arguments and validate the number of arguments
    arguments = sys.argv
    if len(arguments) != 4:
        error("Invalid number of arguments")

    tsvName = arguments[1]
    try:
        number = int(arguments[2])
    except ValueError:
        error("Invalid number argument")
    jsonName = arguments[3]

    # Open the input json file for read
    try:
        tsvFile = open(tsvName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Open the input json file for read
    try:
        jsonFile = open(jsonName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Load and parse tsv data
    reader = csv.reader(tsvFile, delimiter='\t')
    idf = {}
    vector = {'business': [], 'entertainment':[], 'politics':[], 'sport':[], 'tech':[]}
    for row in reader:
        if row[0] == 'idf':
            idf[row[1]] = float(row[2])
        else:
            pairs = row[2].split(', ')
            words = {}
            for pair in pairs:
                pair = pair.split(': ')
                words[pair[0][1:-1]] = float(pair[1])
            vector[row[1]].append(words)
    tsvFile.close()
    """ for i in idf.keys():
        print(i, idf[i])
    print('\n\n\n')
    for i in vector:
        print(i,'\n', vector[i], '\n\n') """

    # Load and parse json data
    jsonData = json.load(jsonFile)
    jsonFile.close()

    KnnInference(tsvFile, number, jsonData)


if __name__ == "__main__":
    main()

    print('\nDone\n')
