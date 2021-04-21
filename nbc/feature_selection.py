import csv, json, nltk, string, sys,math
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
        self.classCount = {'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0,'Total':0}
        self.binCount = {}
        self.vocabCounts={}
        self.kContainer = {'business':{},'entertainment':{},'politics':{},'sport':{},'tech':{}}
        self.topKterms={'business':[],'entertainment':[],'politics':[],'sport':[],'tech':[]}

    def getVocab(self):
        #get vocabulary of Corpus in an unordered set
        for document in self.corpus:
            document['text'] = document['text'].split()            
            for term in document['text']:
                self.size+=1
                term = tokenize(term)
                self.vocab.add(term)

    # binary count of whether or not the term appears in the class.
    def getBinCount(self):
        #get frequency of each term for each class
        for term in self.vocab:
            self.binCount[term]={'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0,'Total':0}
        for document in self.corpus:
            #to avoid repeated terms
            for token in set(document['text']):
                token = tokenize(token)
                self.binCount[token][document['category']]+=1
                self.binCount[token]['Total']+=1
        #print(self.binCount)
        print(self.binCount['the'])

    def getClassCount(self):
        for document in self.corpus:
            docClass = document['category']
            self.classCount[docClass] += 1
            self.classCount['Total'] += 1

    def getMutualInfo(self):
        #total number of documents
        N= len(self.corpus)
        for c in self.classList:
            #self.kContainer[c] = {}
            # Documents that do not contain the term but do contatin the class
            N_0_1 = self.classCount[c] ###################################VERIFY
            
            for term in self.binCount:
                self.kContainer[c][term] = 0
                if term != '':
                     # Documents that contain the term
                    N_1 =self.binCount[term]['Total']
                    #Documents that contain the term and contain the class 
                    N_1_1 = self.binCount[term][c]
                    if N_1_1 == 0:
                        N_1_1=1
                    if self.binCount[term][c] == 0:
                        # Documents that Contain the term but do not contain the class
                        N_1_0 = self.binCount[term]['Total']
                    else:
                        N_1_0=1
                    N_0_1 = N_0_1- self.binCount[term]['Total'] ###################################VERIFY
                    if N_0_1 <1 :
                        N_0_1 =1
                    #documents without term and without class
                    N_0_0 = len(self.corpus) - self.classCount[c] - self.binCount[term]['Total'] ############ VERIFY
                    if N_0_0 < 1:
                        N_0_0 =1
                     #documents that do not have the term
                    N_0 = len(self.corpus)  - self.binCount[term]['Total']
                    if N_0 < 1:
                        N_0 = 1
                    #mutual Information calc split into 4 parts:
                    part_1 =(N_1_1/N)*math.log((N*N_1_1)/N_1*N_1,2)
                    part_2 = (N_0_1/N)*math.log((N*N_0_1)/N_0*N_1,2)
                    part_3 = (N_1_0/N)*math.log((N*N_1_0)/N_1*N_0,2)
                    part_4 =  (N_0_0/N)*math.log((N*N_0_0)/N_0*N_0,2)
                  
                    mutualInfo = part_1 + part_2+ part_3 + part_4 
                    self.kContainer[c][term] = mutualInfo
            print(c)
            
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
            print(c)
            print(self.topKterms[c])


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
    featureSelect.getClassCount()
    featureSelect.getBinCount()
    featureSelect.getMutualInfo()
    featureSelect.selectTopK()
    featureSelect.createOutput(outputName)
if __name__ == "__main__":
    main()
    print('\nDone\n')



