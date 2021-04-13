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
    dictionary = {'doc_id': []}


if __name__ == "__main__":
    main()

    print('\nDone\n')


###########################################################################
#take model from train, 
#produce an output file with same format as input file from train

#calc mutual info of terms and classes
class FeatureSelect:

    def __init__(self, model, vocab):
        self.model = model
        self.k = k
        self.vocab = vocab
        self.L=[]
        self.topFeatures = []

    def selectFeatures(self):
        for term in self.vocab:
            #Compute the terms shared info with each class
            # L.append(argmax(shared information))

    def getTopK(self):
        iter = 0
        while iter <self.k:
            self.topFeatures.append(self.L[iter])
            iter+=1
        
    def createOutput(self):
        for feature in self.topFeatures:
            #write to a file with identical formatting to the training set
            file.write(feasture)
