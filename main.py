#!/usr/bin/env python

from nltk.tokenize import word_tokenize
import email
import os

from preprocess_words import PreprocessWords
from classifier import Classifier

EMAIL_PATH = 'email'

if __name__ == '__main__':
    emails_path = 'spamassasin/spam/'
    all_emails = os.listdir(emails_path)
    email_path = os.path.abspath(os.path.join(emails_path, all_emails[1]))

    classes = ['SPAM', 'HAM']
    c = Classifier(len(classes))

    with open(email_path) as f:
        # Get email's body only, remove header.
        e = email.message_from_string(f.read())
        body = e.get_payload()
        body_words = word_tokenize(body)
        pw = PreprocessWords()
        words = set(pw.words_process(body_words))
        print words
        c.train(words, 0)
