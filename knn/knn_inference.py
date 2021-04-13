#take in model -->output predictions

class KnnInference:

    def __init__(self, model, k,testCorpus):
        self.model=model
        self.k=k
        self.testCorpus=testCorpus

    def applyKnn(self):
        #for each doc?? find the nearest neighbor
        for each class get argmax 