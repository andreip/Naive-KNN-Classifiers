from math import log
import operator

class KNNClassifier:
    '''K Nearest-Neighbor classifier.'''
    def __init__(self, k):
        self.k = k
        self.freq = {}
        self.train_data = []

    def train(self, words, cls):
        '''Receive a bunch of data and store it together with the class.
        Then on query, find the nearest one(s) and do a mean between them
        to get the resulting class.
        '''
        for word in words:
            self.freq[word] = self.freq.get(word, 0) + 1
        self.train_data.append((set(words), cls))

    def classify(self, words):
        '''Find the class based on finding the k-nearest
        and getting the class from the k-nearest's classes.
        '''
        results = []
        for data, cls in self.train_data:
            # Gather all common words with this data.
            # Because data is a set, it's more efficient to do if
            # membership this way than doing "if x in words".
            common_words = [x for x in words if x in data]

            score = 0.0
            nr = float(len(self.train_data))
            for word in common_words:
                score += log(nr / self.freq[word])
            results.append((score, cls))

        # Sort them descending by score.
        results.sort(reverse=True)

        # Look at top K results and return the class.
        return self.get_class(results[:self.k])

    def get_class(self, results):
        '''Return the class that appears the most.'''
        counts = {}
        for _, cls in results:
            counts[cls] = counts.get(cls, 0) + 1
        return max(counts.iteritems(), key=operator.itemgetter(1))[0]
