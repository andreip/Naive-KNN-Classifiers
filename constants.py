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
