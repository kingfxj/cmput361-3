import csv, json, nltk, string, sys
from os import path


def error(name):
    #Print out the error and exit the program with -1
    #input: name is the name of the error
    print(name, file=sys.stderr)
    exit(-1)

# Tokenize the list value
def tokenize(word):
    # Lemmatize the word
    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    word = nltk.WordNetLemmatizer().lemmatize(word)
    # Remove punctuations and make all words lower case
    return word
#take model from train, 
#produce an output file with same format as input file from train

#calc mutual info of terms and classes
class FeatureSelect:

    def __init__(self,corpus,k):
        self.k = k
        self.corpus = corpus
        self.vocab = set()
        self.size = 0
        self.freqDist = {}
        self.vocabCounts={}
        self.kContainer = {}

    #get vocabulary of Corpus in an unordered set
    def getVocab(self):
        for document in self.corpus:
            document['text'] = document['text'].split()            
            for term in document['text']:
                self.size+=1
                term = tokenize(term)
                self.vocab.add(term)
    def getFreq(self):
        for term in self.vocab:
            self.freqDist[term]={'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0,'Total':0}
        for document in self.corpus:
            for token in document['text']:
                token = tokenize(token)
                self.freqDist[token][document['category']]+=1
                self.freqDist[token]['Total']+=1

    def getMutualInfo(self):
        print(self.freqDist)
        for term in self.freqDist:
            for c in self.freqDist[term]:
                self.kContainer[c] = {term:self.freqDist[term][c]}
            #Compute the terms shared info with each class
            # L.append(argmax(shared information))

        print(self.kContainer)
    def createOutput(self,trainData,file):
        with open(file, 'w') as outfile:
            for i in range(len(trainData)):
                json.dump(trainData[i], outfile)
                json.dump('\n', outfile)      

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

    # Load and parse json data
    inputData = json.load(inputFile)
    inputFile.close()

    featureSelect = FeatureSelect(inputData,number)
    featureSelect.getVocab()
    featureSelect.getFreq()
    featureSelect.getMutualInfo()
    #featureSelect.createOutput(inputData,outputName)
if __name__ == "__main__":
    main()
    print('\nDone\n')



