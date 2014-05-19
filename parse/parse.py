class Parse:
    @staticmethod
    def get_parsed_texts(path):
        '''Given a path for a file, read it and return an array of the form
        text,class.

        Returns:
             [ [text1, class1], [text2, class2], ... ].
        '''
        raise NotImplementedError, 'Use a non-abstract parser for what you need.'
