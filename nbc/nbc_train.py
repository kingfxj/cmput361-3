import csv, json, math, nltk, string, sys
from nltk import WordNetLemmatizer
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
    # Remove punctuations and make all words lower case
    return word


class Train:
    def __init__(self,corpus):
        self.corpus = corpus
        self.priors= {'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0,'Total':0}
        self.likelihoods = []
        self.vocab = set()
        self.size = 0
        self.freqDist = {}
        self.vocabCounts={}

    # Get vocabulary of Corpus in an unordered set
    def getVocab(self):
        for document in self.corpus:
            document['text'] = document['text'].split()            
            for term in document['text']:
                self.size+=1
                term = tokenize(term)
                self.vocab.add(term)
    
    # Get occurances of each token in each class
    def getFreq(self):
        for term in self.vocab:
            self.freqDist[term]={'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0,'Total':0}

        for document in self.corpus:
            for token in document['text']:
                token = tokenize(token)
                self.freqDist[token][document['category']]+=1
                self.freqDist[token]['Total']+=1

    # For each class get prior probability
    def getPriors(self,writer):
        for document in self.corpus:
            self.priors[document['category']]+=1
            self.priors['Total']+=1
        for key in self.priors:
            if key != 'Total':
                writer.writerow(['prior',key,math.log(self.priors[key]/self.priors['Total'],2)])

    # Get conditional probability for each token in each class
    def getLikelihood(self, writer):
        for word in self.freqDist:
            for category in self.freqDist[word]:
                if category != 'Total' and word != '':
                    self.freqDist[word][category]+=1
                    divisor = self.size +1
                    writer.writerow(['likelihood',category,word,math.log(self.freqDist[word][category]/divisor,2)])
        
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
            user = input('Do you want to replace the file: '+ outputName + '?\n').lower()
            if user in ['no', 'n']:
                print('Mission aborted')
                inputFile.close()
                return
            elif user in ['yes', 'y']:
                break

    try:
        outputFile = open(outputName, 'w', newline='')
    except IOError:
        error('Invalid output file argument')

    # Load and parse json data
    inputData = json.load(inputFile)
    inputFile.close()

    theWriter = csv.writer(outputFile, delimiter='\t')

    train = Train(inputData)
    train.getVocab()
    train.getFreq()
    train.getPriors(theWriter)
    train.getLikelihood(theWriter)
 
    outputFile.close()


if __name__ == "__main__":
    main()

    print('\nDone\n')
