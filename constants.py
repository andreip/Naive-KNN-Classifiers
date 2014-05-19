MAIL_CLASSES = ['SPAM', 'HAM']
MAIL_TRAIN_CONFIG = [
    # (PATH, CLASS), 0 - SPAM, 1 - HAM
    'spamassasin/train/spam',
    'spamassasin/train/spam_2',
    'spamassasin/train/ham',
    'spamassasin/train/ham_2',
    'spamassasin/train/ham_hard',
]
MAIL_TEST_CONFIG = [
    'spamassasin/test/spam',
    'spamassasin/test/spam_2',
    'spamassasin/test/ham',
    'spamassasin/test/ham_2',
    'spamassasin/test/ham_hard',
]

ROTTEN_CLASSES = ['negative', 'somewhat negative', 'neutral', 'somewhat positive',
           'positivie']
ROTTEN_TRAIN_CONFIG = [
    'rotten_tomatoes/train',
]
ROTTEN_TEST_CONFIG = [
    'rotten_tomatoes/test',
]
