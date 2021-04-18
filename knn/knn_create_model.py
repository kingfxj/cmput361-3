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
   
# Take train corpus --> output to CSV

class KnnModel:
    def __init__(self,corpus, outputFile):
        self.corpus = corpus
        self.document = []
        self.IdfLines = []
        self.VectorLines = []
        self.outputFile = outputFile
    
    def vectorize(self):
        for document in self.corpus:
            #represent as a vector using ltn wieght scheme
            self.document.append(document)

    def getIdf(self):
        for _ in self.document:
            self.outputFile.writerow(["IDF", "term", "IDFWeight"])

    def getVector(self):
        #for class in model:
        self.outputFile.writerow(["Vectpr", "class", "STRING REPRESENTATION OF VECTOR FOR CLASS"])


def main():
    # Get the arguments and validate the number of arguments
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid number of arguments")

    inputName = arguments[1]
    outputName = arguments[2]

    # Open the input json file for read
    try:
        inputFile = open(inputName, 'r')
    except IOError:
        error('Invalid input file argument')

    # Open the output file for write
    if path.exists(outputName):
        while True:
            user = input('Do you want to replace the file: ' + outputName + '?\n').lower()
            if user in ['no', 'n']:
                print('Mission aborted')
                inputFile.close()
                return
            elif user in ['yes', 'y']:
                break

    try:
        outputFile = open(outputName, 'w', newline='')
    except IOError:
        error('Invalid putput file argument')

    # Load and parse json data
    inputData = json.load(inputFile)
    inputFile.close()

    theWriter = csv.writer(outputFile, delimiter='\t')
    theWriter.writerow(['ID', 'normalized weight'])

    knn = KnnModel(inputData, theWriter)
    knn.vectorize()
    knn.getIdf()
    knn.getVector()

    outputFile.close()


if __name__ == "__main__":
    main()

    print('\nDone\n')
