import csv, json, nltk, string, sys,math

def error(name):
    #Print out the error and exit the program with -1
    #input: name is the name of the error
    print(name, file=sys.stderr)
    exit(-1)

# Tokenize the list value
def tokenize(word):
    # Remove punctuations and make all words lower case 
    # Lemmatize the word
    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    word = nltk.WordNetLemmatizer().lemmatize(word)
    return word

def listToDict(array):
    #convert the data from tsv into a dictionary for each term.
    likelihoodDict = {}
    for i in array:
        likelihoodDict[i[2]]={'business':0,'entertainment':0,'politics':0,'sport':0,'tech':0}
    for i in array:
        if likelihoodDict[i[2]][i[1]]== 0:
            likelihoodDict[i[2]][i[1]] = math.log(float(i[3]),2)
    return likelihoodDict


class Test:

    def __init__(self,prior,likelihood,testCorpus):
        self.priors = prior
        self.likelihoods = likelihood
        self.testCorpus = testCorpus
        self.stats ={'business': {'TP':0 ,'TN':0 , 'FP':0, 'FN':0},
                    'entertainment':{'TP':0,'TN':0,'FP':0,'FN':0},
                    'politics':{'TP':0,'TN':0,'FP':0,'FN':0},
                    'sport':{'TP':0,'TN':0,'FP':0,'FN':0},
                    'tech': {'TP':0,'TN':0,'FP':0,'FN':0}}
        self.precisions = {'business': 0,
                    'entertainment':0,
                    'politics':0,
                    'sport':0,
                    'tech': 0}
        self.recalls = {'business': 0,
                    'entertainment':0,
                    'politics':0,
                    'sport':0,
                    'tech': 0}
        # All values init to 0
        self.F1s = {'business': 0,
                    'entertainment':0,
                    'politics':0,
                    'sport':0,
                    'tech': 0}

    def cleanText(self):
        #tokenize the test data as we did witht the train
        for document in self.testCorpus:
            document['text'] = document['text'].split()            
            for term in document['text']:
                if term[-1]=='.':
                    term=term[0:-1]
                term = tokenize(term)

    def getScores(self):
        #get counts for each document class
        for document in self.testCorpus:
            category = document['category']
            score = {}
            for c in self.priors:
                score[c] = self.priors[c]
                for term in document['text']:
                    #what to do with out of vocab terms?????????
                    if term in self.likelihoods.keys():
                        score[c] += self.likelihoods[term][c]
            prediction = max(score,key=score.get)
            if category == prediction:
                self.stats[category]['TP']+=1
                for key in self.stats.keys():
                    if key!= category:
                        self.stats[key]['TN']+=1  
            if category != prediction:
                self.stats[prediction]['FP']+=1
                self.stats[category]['FN']+=1

    def getStats(self):
        #get various required statistics for each class
        print('\nCounts:')
        for key in self.stats.keys():
            print(str(key) + str(self.stats[key]))
        print('\nPrecisions:')
        for key in self.stats.keys():
            self.precisions[key]= self.stats[key]['TP']/(self.stats[key]['TP']+self.stats[key]['FP'])
            print('Precision: '+str(key) + ' ' +str(self.precisions[key]))
        print('\nRecalls:')
        for key in self.stats.keys():
            self.recalls[key]= self.stats[key]['TP']/(self.stats[key]['TP']+self.stats[key]['FN'])
            print('Recall: '+str(key) + ' ' +str(self.recalls[key]))
        print('\nF1s:')
        for key in self.stats.keys():
            self.F1s[key] = (2*(self.precisions[key]*self.recalls[key])/self.precisions[key]+self.recalls[key])
            print('F1: '+str(key) + ' ' +str(self.F1s[key]))
        print('\nMicroaverage F1:')
        #micro and macro F1
        TP = 0
        FP = 0
        FN = 0
        for key in self.stats.keys():
            TP += self.stats[key]['TP']
            FP += self.stats[key]['FP']
            FN += self.stats[key]['FN']
        prec = TP/(TP+FP)
        rec = TP/(TP+FN)
        microF1 = (2*(prec*rec)/(prec+rec))
        print(str(microF1))
        print('\n Macroaverage F1:')
        macroF1 = 0
        for key in self.F1s.keys():
            print(self.F1s[key])
            macroF1 +=self.F1s[key]
        macroF1 = macroF1/5
        print(str(macroF1))


def main():
    # Get the arguments and validate the number of arguments
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid number of arguments")

    tsvName = arguments[1]
    jsonName = arguments[2]

    # Open the input tsv file for read
    try:
        tsvFile = open(tsvName, 'r')
    except IOError:
        error('Invalid tsv file argument')

    # Open the json tsv file for read
    try:
        jsonFile = open(jsonName, 'r')
    except IOError:
        error('Invalid json file argument')

    csvReader = csv.reader(tsvFile, delimiter='\t')

    prior = {}
    likelihood = []
    for row in csvReader:
        if row[0] == 'prior':
            prior[row[1]] = math.log(float(row[2]),2)
        else:
            likelihood.append(row)

    # Open the json tsv file for read
    try:
        jsonFile = open(jsonName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    jsonData = json.load(jsonFile)
    jsonFile.close()
    likelihood = listToDict(likelihood)
    test = Test(prior,likelihood,jsonData)
    test.cleanText()
    test.getScores()
    test.getStats()

if __name__ == "__main__":
    main()
    print('\nDone\n')