import os

from parse import Parse

class RottenTomatoesParse(Parse):
    @staticmethod
    def get_parsed_texts(path):
        with open(path) as f:
            # Ignore firest line
            f.readline()
            # Format of line: PhaseId\tSentenceId\tPhase\tSentiment\n
            lines = map(RottenTomatoesParse.parse_line, f.readlines())
        return lines

    @staticmethod
    def parse_line(line):
        line = line.strip('\n').split('\t')[2:]
        # In case we've got a class, that one should be an index (integer).
        if len(line) == 2:
            line[1] = int(line[1])
        # We don't know the class in advance, mark as unknown.
        else:
            line.append(None)
        return line

#testing
#print RottenTomatoesParse.get_parsed_texts('rotten.tsv')
