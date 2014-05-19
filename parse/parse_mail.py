import email
from os.path import dirname, basename

from constants import MAIL_CLASSES
from parse import Parse

class MailParse(Parse):
    @staticmethod
    def get_parsed_texts(path):
        dir_name = basename(dirname(path)).lower()
        # The index of the found class
        cls = 0 if MAIL_CLASSES[0].lower() in dir_name else 1

        with open(path) as f:
            text = f.read()

            # Get email's body only, remove header.
            e = email.message_from_string(text)
            body = e.get_payload()
            if isinstance(body, list):
                body = ''.join(map(str, body))

        return [[body, cls]]

#testing
#print MailParse.get_parsed_texts('spamassasin/test/ham/00701.4c1a296394c3afdcb38020e8283d1a5d')
