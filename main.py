import email
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

EMAIL_PATH = 'email'
COMMON_WORDS = ['the', 'and', 'of', 'or']
MIN_WORD_LEN = 2

stemmer = SnowballStemmer("english")

def keep_only_letters(word):
    '''Given a string like "ana1.bbc", return "anabbc".'''
    letter = lambda c : 'a' <= c <= 'z' or 'A' <= c <= 'Z'
    return filter(letter, word)

def not_common_word(word):
    return word != COMMON_WORDS

def not_too_short(word):
    return len(word) > MIN_WORD_LEN

if __name__ == '__main__':
    with open(EMAIL_PATH) as f:
        # Get email's body only, remove header.
        e = email.message_from_string(f.read())
        body = e.get_payload()
        body_words = word_tokenize(body)
        # Keep only alphabetic, remove punctuation, numbers, lowercase
        # everything.
        body_alpha = map(keep_only_letters, body_words)
        body_alpha = map(lambda word: word.lower(), body_alpha)
        # Remove common words from english grammar.
        body_no_common_words = filter(not_common_word, body_alpha)
        # Stem all words from body.
        body_stemmed = filter(stemmer.stem, body_no_common_words)
        body = filter(not_too_short, body_stemmed)
        print body
