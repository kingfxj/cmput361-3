import csv, json, nltk, string, sys
from math import log10
from os import path


def error(name):
    '''
    Print out the error and exit the program with -1
    input: name is the name of the error
    '''
    print(name, file=sys.stderr)
    exit(-1)


# Tokenize the list value
def tokenize(word):
    # Lemmatize the word
    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    word = nltk.WordNetLemmatizer().lemmatize(word)
    return word
   
# Take train corpus --> output to CSV

class KnnModel:
    def __init__(self, corpus, outputFile):
        self.corpus = corpus
        self.documents = []
        self.dict = {}
        self.size = 0
        self.IdfLines = {}
        self.VectorLines = []
        self.outputFile = outputFile
    
    def vectorize(self):
        for document in self.corpus:
            self.size += 1
            document['text'] = document['text'].split()
            vocab = {}
            for term in document['text']:
                term = tokenize(term)
                if term in vocab:
                    vocab[term] += 1
                else:
                    vocab[term] = 1
                    if term in self.dict:
                        self.dict[term] += 1
                    else:
                        self.dict[term] = 1
            #represent as a vector using ltn wieght scheme
            self.documents.append([document['category'], vocab])

    def getIdf(self):
        for word in sorted(self.dict.keys()):
            # print(word, self.vocab[word])
            if len(word) != 0:
                self.outputFile.writerow(["idf", word, log10(self.size / self.dict[word])])

    def getVector(self):
        #for class in model:
        for document in self.documents:
            vector = {}
            for word in sorted(document[1].keys()):
                if len(word) != 0:
                    log = 1 + log10(document[1][word])
                    idf = log10(self.size / self.dict[word])
                    vector[word] = log * idf
            self.outputFile.writerow(["vector", document[0], str(vector)[1:-1]])


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

    knn = KnnModel(inputData, theWriter)
    knn.vectorize()
    knn.getIdf()
    knn.getVector()

    outputFile.close()


if __name__ == "__main__":
    main()

    print('\nDone\n')
