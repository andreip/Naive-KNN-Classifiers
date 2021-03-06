#!/usr/bin/env python

from nltk.tokenize import word_tokenize
import os, sys

from preprocess_words import PreprocessWords
from classifier.naive_bayes_classifier import NaiveBayesClassifier
from classifier.knn_classifier import KNNClassifier

from constants import *
from parse.parse_mail import MailParse
from parse.parse_rotten_tomatoes import RottenTomatoesParse

def do_with_config(config, classifier, preprocessor, parser, train=True):
    for path in config:
        classified_wrong = 0

        # Get all files from local directory
        all_data_files = os.listdir(path)

        string = 'training' if train else 'classifying'
        print string + ' size ' + str(len(all_data_files)) + ' (' +\
              path + ') ...',
        sys.stdout.flush()

        # For each training data from the provided path
        # get abs path and load data from file, parse it
        # and serve it to classifier.
        for data_file in all_data_files:
            abs_path = os.path.abspath(os.path.join(path, data_file))

            for text, cls in parser.get_parsed_texts(abs_path):
                words = word_tokenize(text)
                #words = set(preprocessor.process_words(words))
                words = preprocessor.process_words(words)
                if train:
                    classifier.train(words, cls)
                else:
                    got_cls = classifier.classify(words)
                    # Count how many results we got the class wrong.
                    if cls != None:
                        classified_wrong += got_cls != cls
                    # Print the result, we cannot account for the class
                    # right/wrong as we don't know it.
                    else:
                        print got_cls, words

        # Print info.
        print 'Done.'
        if not train:
            print 'got wrong ' + str(classified_wrong)

def do_exit():
    print 'call like\n\t./main {TYPE=rotten/mail} {CLS=naive/knn} [K=integer (for KNN)]'
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        do_exit()

    if sys.argv[1] == 'rotten':
        cls, train, test = ROTTEN_CLASSES, ROTTEN_TRAIN_CONFIG, ROTTEN_TEST_CONFIG
        parser = RottenTomatoesParse
    elif sys.argv[1] == 'mail':
        cls, train, test = MAIL_CLASSES, MAIL_TRAIN_CONFIG, MAIL_TEST_CONFIG
        parser = MailParse
    else:
        do_exit()

    if sys.argv[2] == 'naive':
        classifier = NaiveBayesClassifier(len(cls))
    elif sys.argv[2] == 'knn':
        # Read K from CLI if provided.
        if len(sys.argv) > 3:
            k = int(sys.argv[3])
        else:
            k = 5
        classifier = KNNClassifier(k)
    else:
        do_exit()

    # The classifier will learn once we feed it with data.
    preprocessor = PreprocessWords()

    do_with_config(train, classifier, preprocessor, parser, True)
    do_with_config(test, classifier, preprocessor, parser, False)
