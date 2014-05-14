from nltk.tokenize import word_tokenize
import email

from preprocess_words import PreprocessWords

EMAIL_PATH = 'email'

if __name__ == '__main__':
    with open(EMAIL_PATH) as f:
        # Get email's body only, remove header.
        e = email.message_from_string(f.read())
        body = e.get_payload()
        body_words = word_tokenize(body)
        pw = PreprocessWords()
        words = pw.words_process(body_words)
        print words
