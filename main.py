#!/usr/bin/env python

from nltk.tokenize import word_tokenize
import email
import os

from preprocess_words import PreprocessWords
from classifier import Classifier

CLASSES = ['SPAM', 'HAM']
TRAIN_CONFIG = [
    # (PATH, CLASS), 0 - SPAM, 1 - HAM
    ('spamassasin/train/spam', 0),
    ('spamassasin/train/spam_2', 0),
    ('spamassasin/train/ham', 1),
    ('spamassasin/train/ham_2', 1),
    ('spamassasin/train/ham_hard', 1),
]
TEST_CONFIG = [
    ('spamassasin/test/spam', 0),
    ('spamassasin/test/spam_2', 0),
    ('spamassasin/test/ham', 1),
    ('spamassasin/test/ham_2', 1),
    ('spamassasin/test/ham_hard', 1),
]

def do_with_config(config, classifier, preprocessor, train=True):
    for path, cls in config:
        classified_wrong = 0
        total = 0

        # Get all files from local directory
        all_data_files = os.listdir(path)

        string = 'training' if train else 'classifying'
        print string + ' size ' + str(len(all_data_files)) + ' (' +\
              CLASSES[cls] + ') ...',

        # For each training data from the provided path
        # get abs path and load data from file, parse it
        # and serve it to classifier.
        for data_file in all_data_files:
            abs_path = os.path.abspath(os.path.join(path, data_file))

            with open(abs_path) as f:
                # Get email's body only, remove header.
                e = email.message_from_string(f.read())

                body = e.get_payload()
                if isinstance(body, list):
                    body = ''.join(map(str, body))

                body_words = word_tokenize(body)
                #words = set(preprocessor.process_words(body_words))
                words = preprocessor.process_words(body_words)
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
    classifier = Classifier(len(CLASSES))
    preprocessor = PreprocessWords()

    do_with_config(TRAIN_CONFIG, classifier, preprocessor, True)
    do_with_config(TEST_CONFIG, classifier, preprocessor, False)
