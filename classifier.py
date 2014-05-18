from collections import defaultdict
import math

class Classifier:
    def __init__(self, nr_classes):
        # Classes 
        self.nr_classes = nr_classes
        # For every class keep record of how many examples
        # does it have and how many words does it have (from examples).
        self.examples_count = [0 for _ in range(self.nr_classes)]
        self.words_count = [0 for _ in range(self.nr_classes)]
        # Keep a record of every data and how many times it
        # is classified in every class.
        self.data_dict = defaultdict(lambda: [0 for _ in
                                     range(self.nr_classes)])

    def train(self, training_data, cls):
        '''Provide a list of data to keep a record of,
        and the class the data fits in.

        Class must be an index between [0, nr_classes).
        '''
        # Increment the number of appearances for every data
        # in the given class.
        for data in training_data:
            self.data_dict[data][cls] += 1

        # Keep the number of usages for a given class so we can
        # calculate its probability easily in classify.
        self.words_count[cls] += len(training_data)
        self.examples_count[cls] += 1

    def classify(self, data):
        '''Returns a class for a given data based on
        self.data_dict, using bayesian and considering
        conditional independence between stored data (naive).

        * find the max p(class|data) and return class.
        * this is p(class|data) = p(data|class) * p(class) / p(data)
          from Bayes Rule ; but because we're looking for maximizing
          around class for p(class|data), then the denominator p(data)
          can be removed
          => p(class|data) = p(data|class) * p(class)
                           = p(w1, w2, ... wn | class) * p(class),
             where the data (e.g. a mail) can be composed of words.
                           = p(w1 | class) * ... p(wn | class) * p(class),
             and the above step is the _naive_ assumption.

             Actually it's naive because it's simpler, it's an approximation,
             but works well in practice.
        '''

        # Find the class that maximizes the probability p(class|data).
        max_cls = max_prob = -1
        for cls in range(self.nr_classes):
            probabilities = []

            # Calculate p(cls).
            p = self.calc_prob(self.examples_count[cls],
                               sum(self.examples_count), self.nr_classes)
            probabilities.append(p)

            # Calculate p(w1|cls), p(w2|cls) ...
            for word in data:
                # The nr of classes here is the nr of distinct words.
                nr_classes = len(self.data_dict)
                p = self.calc_prob(self.data_dict[word][cls],
                                   self.words_count[cls], nr_classes)
                probabilities.append(p)

            # Keep the biggest probability among all.
            probability = self.calc_total_prob(probabilities)

            #print 'obtained (prob, cls)', probability, cls

            if max_prob < probability or max_cls == -1:
                max_prob = probability
                max_cls = cls

        return max_cls

    def calc_total_prob(self, probabilities):
        '''Given a list of probabilities, do sth with them and obtain
        a single number. In our case we shall not do
        p = p1 * p2 * ... * pn, for pi in probabilities, but
        p = log(p1) + log(p2) + ... + log(pn), for pi in probabilities
        because the former one goes very close to 0 and it appears
        floating point representation error.
        '''
        return sum(map(math.log, probabilities))

    def calc_prob(self, nominator, denominator, nr_classes, k=1):
        '''Calculates the probability:
                 nominator
            p = -----------
                denominator

         but also adds laplace smoothing, so:
                      nominator + k
            p = ----------------------------
                denominator + k * nr_classes
        '''
        return float(nominator + k) / (denominator + k * nr_classes)
