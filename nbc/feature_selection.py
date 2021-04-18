import csv, json, nltk, string, sys
from os import path


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
        error("Invalid number of arguments")

    inputName = arguments[1]
    try:
        number = int(arguments[2])
    except ValueError:
        error('Invalid number argument')
    outputName = arguments[3]

    for _ in range(number):
        pass

    # Open the input json file for read
    try:
        inputFile = open(inputName, 'r')
    except IOError:
        error('Invalid input file argument')

    if path.exists(outputName):
        while True:
            user = input('Do you want to replace the file: ' + outputName + '?\n').lower()
            if user in ['no', 'n']:
                print('Mission aborted')
                inputFile.close()
                return
            elif user in ['yes', 'y']:
                break


    # Open the output json file for write
    try:
        outputFile = open(outputName, 'w')
    except IOError:
        error('Invalid output file argument')

    # Load and parse json data
    inputData = json.load(inputFile)
    inputFile.close()
    # print(inputData)
    for _ in inputData:
        pass

    outputFile.close()


###########################################################################
# Take model from train, 
# Produce an output file with same format as input file from train

# Calc mutual info of terms and classes
class FeatureSelect:

    def __init__(self, model, vocab):
        self.model = model
        self.k = 0
        self.vocab = vocab
        self.L=[]
        self.topFeatures = []

    def selectFeatures(self):
        for term in self.vocab:
            #Compute the terms shared info with each class
            # L.append(argmax(shared information))
            print(term)

    def getTopK(self):
        iter = 0
        while iter <self.k:
            self.topFeatures.append(self.L[iter])
            iter+=1
        
    def createOutput(self, outputFile):
        for feature in self.topFeatures:
            #write to a file with identical formatting to the training set
            outputFile.write(feature)


if __name__ == "__main__":
    main()

    print('\nDone\n')
