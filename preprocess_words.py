from nltk.stem.snowball import SnowballStemmer

class PreprocessWords:
    COMMON_WORDS = ['the', 'and', 'of', 'or']
    MIN_WORD_LEN = 2

    def __init__(self):
        self.stemmer = SnowballStemmer("english")
        self.stopwords = open(r'stopwords.txt', 'r').read().splitlines()

    def process_words(self, words):
        '''Returns a list of words that go through: tokenization,
        lowercase, keeping only letters and stemming.'''
        # Keep only alphabetic, remove punctuation, numbers, lowercase
        # everything.
        words = map(self.keep_only_letters, words)
        words = map(lambda word: word.lower(), words)
        # Remove common words from english grammar.
        words = filter(self.not_common_word, words)
        # Keep only long enough words.
        words = filter(self.not_too_short, words)
        # Stem all words from body.
        words = filter(self.stemmer.stem, words)
        # Remove duplicates.
        words = list(set(words))
        return words

    def keep_only_letters(self, word):
        '''Given a string like "ana1.bbc", return "anabbc".'''
        letter = lambda c : 'a' <= c <= 'z' or 'A' <= c <= 'Z'
        return filter(letter, word)

    def not_common_word(self, word):
        return word not in self.stopwords

    def not_too_short(self, word):
        return len(word) > self.MIN_WORD_LEN

