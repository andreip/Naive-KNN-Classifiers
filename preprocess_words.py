from nltk.stem.snowball import SnowballStemmer

class PreprocessWords:
    COMMON_WORDS = ['the', 'and', 'of', 'or']
    MIN_WORD_LEN = 2

    def __init__(self):
        self.stemmer = SnowballStemmer("english")

    def words_process(self, words):
        '''Returns a list of words that go through: tokenization,
        lowercase, keeping only letters and stemming.'''
        # Keep only alphabetic, remove punctuation, numbers, lowercase
        # everything.
        words = map(self.keep_only_letters, words)
        words = map(lambda word: word.lower(), words)
        # Remove common words from english grammar.
        words_no_common = filter(self.not_common_word, words)
        # Stem all words from body.
        words_stemmed = filter(self.stemmer.stem, words_no_common)
        words = filter(self.not_too_short, words_stemmed)
        return words

    def keep_only_letters(self, word):
        '''Given a string like "ana1.bbc", return "anabbc".'''
        letter = lambda c : 'a' <= c <= 'z' or 'A' <= c <= 'Z'
        return filter(letter, word)

    def not_common_word(self, word):
        return word != self.COMMON_WORDS

    def not_too_short(self, word):
        return len(word) > self.MIN_WORD_LEN

