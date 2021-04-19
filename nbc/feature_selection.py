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

class FeatureSelect:

    def __init__(self,corpus,k):
        self.classList = ['business','entertainment','politics','sport','tech']
        self.k = k
        self.corpus = corpus
        self.vocab = set()
        self.size = 0
        self.freqDist = {}
        self.vocabCounts={}
        self.kContainer = {}
        self.topKterms={'business':[],'entertainment':[],'politics':[],'sport':[],'tech':[]}

    def getVocab(self):
        #get vocabulary of Corpus in an unordered set
        for document in self.corpus:
            document['text'] = document['text'].split()            
            for term in document['text']:
                self.size+=1
                term = tokenize(term)
                self.vocab.add(term)

    def getFreq(self):
        #get frequency of each term for each class
        for term in self.vocab:
            self.freqDist[term]={'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0,'Total':0}
        for document in self.corpus:
            for token in document['text']:
                token = tokenize(token)
                self.freqDist[token][document['category']]+=1
                self.freqDist[token]['Total']+=1

    def getMutualInfo(self):
        #currently just finds the most frequently occuring k items 
        
        for c in self.classList:
            self.kContainer[c] = {}
            for term in self.freqDist:
                if term != '':
                    self.kContainer[c][term] = self.freqDist[term][c]


    def selectTopK(self):
        #for each class, find the K number of terms that share the most mutual unfo with tthat class
        for c in self.classList:
            count = 0
            while count < self.k:
                maxInfo ={'placeHolder':0} 

                for term in self.kContainer[c]:
                    comp = [maxInfo[key] for key in maxInfo.keys()][0]
                    if self.kContainer[c][term]>comp:
                        maxInfo = {term: self.kContainer[c][term]}

                for i in maxInfo.keys():
                    self.kContainer[c].pop(i)
                termToAdd = [key for key in maxInfo.keys()][0]
                self.topKterms[c].append(termToAdd)
                count +=1



    def createOutput(self,file):
        #create a new training file with only the Top K included
        listToWrite = []
        for document in self.corpus:
            category = document['category']
            docToWrite = {'category':category,'text':[]}
            for term in document['text']:
                if term in self.topKterms[category]:
                    docToWrite['text'].append(term)
            s = ' '
            docToWrite['text'] = s.join(docToWrite['text'])
            listToWrite.append(docToWrite)
        with open(file, 'w') as outfile:
            json.dump(listToWrite,outfile,ensure_ascii=False,indent = 4 )


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
    featureSelect.selectTopK()
    featureSelect.createOutput(outputName)
if __name__ == "__main__":
    main()
    print('\nDone\n')



