class Classifier:
    def __init__(self, nr_classes):
        # Classes 
        self.nr_classes = nr_classes
        # Keep a record of every class how many times
        # do we find it in our trainging examples.
        self.classes_count = [0 for _ in range(self.nr_classes)]
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
        # TODO
        pass
