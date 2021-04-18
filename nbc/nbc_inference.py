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
    if len(arguments) != 3:
        error("Invalid arguments")

    tsvName = arguments[1]
    jsonName = arguments[2]

    # Open the input tsv file for read
    try:
        tsvFile = open(tsvName, 'r')
    except IOError:
        error('Invalid file arguments')
    print(tsvFile)
    csvReader = csv.reader(tsvFile, delimiter='\t')
    prior = {}
    likelihood = {}
    for row in csvReader:
        if len(row) == 3:
            prior[row[1]] = float(row[2])
        else:
            likelihood[row[2]] = [row[2], float(row[3])]
    print(prior, '\n')
    for i in prior.keys():t
        print(i, prior[i])
    # print(likelihood)
    for i in likelihood.keys():
        print(i, likelihood[i])

    # Open the json tsv file for read
    try:
        jsonFile = open(jsonName, 'r')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    jsonData = json.load(jsonFile)
    test = Test()


if __name__ == "__main__":
    main()

    print('\nDone\n')

#####################################
#model imported from the TSV created in train

class Test:

    def __init__(self,model,testCorpus):
        self.model = model
        self.testCorpus = testCorpus
        self.busStats = {'TP':0, 'TN':0, 'FP':0, 'FN':0}
        self.entertainStats = {'TP':0, 'TN':0, 'FP':0, 'FN':0}
        self.poliStats = {'TP':0, 'TN':0, 'FP':0, 'FN':0}
        self.sportStats = {'TP':0, 'TN':0, 'FP':0, 'FN':0}
        self.techStats = {'TP':0, 'TN':0, 'FP':0, 'FN':0}
    
    def argmax(self, model):
        return False
    
    def run(self):
        for document in self.testCorpus:
            for term in document:
                predClass = self.argmax(term)
                if predClass == document.category:
                    #do the stats
                    pass

    def getStats(self):
        # for each class:
            #return TP,TN, FP,FN
            #calc F1 macro
            #calc F1 Micro
        pass
