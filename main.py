#!/usr/bin/env python

from nltk.tokenize import word_tokenize
import os, sys

from preprocess_words import PreprocessWords
from classifier import Classifier

from constants import MAIL_CLASSES, MAIL_TRAIN_CONFIG, MAIL_TEST_CONFIG
from parse.parse_mail import MailParse

def do_with_config(config, classifier, preprocessor, train=True):
    for path in config:
        classified_wrong = 0
        total = 0

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

            for text, cls in MailParse.get_parsed_texts(abs_path):
                words = word_tokenize(text)
                #words = set(preprocessor.process_words(words))
                words = preprocessor.process_words(words)
                if train:
                    classifier.train(words, cls)
                else:
                    got_cls = classifier.classify(words)
                    classified_wrong += got_cls != cls
            total += 1

        # Print info.
        print 'Done.'
        if not train:
            print 'got wrong ' + str(classified_wrong)

if __name__ == '__main__':
    # The classifier will learn once we feed it with data.
    classifier = Classifier(len(MAIL_CLASSES))
    preprocessor = PreprocessWords()

    do_with_config(MAIL_TRAIN_CONFIG, classifier, preprocessor, True)
    do_with_config(MAIL_TEST_CONFIG, classifier, preprocessor, False)
