import re, random


def main():
    # Data can be coming from local file for now
    filename = 'text-file.txt'
    textContent = readText(filename)

    database = Database()

    words = re.findall(r'\b\w+\b', textContent)
    firstWord = words[random.randrange(0, len(words))]

    # TODO: remove side-effects, refactor to functional form
    processWords(words, database)

    secondWord = database.findSecondWord(firstWord)
    
    sentence = f'{firstWord} {secondWord}'

    # configuration
    sentenceLength = 10
    for i in range(sentenceLength - 2):
        nextWord = database.findNextWord(firstWord, secondWord)
        sentence = f'{sentence} {nextWord}'

        firstWord = secondWord
        secondWord = nextWord

    print(sentence)


def readText(filename):
    with open(filename) as input_file:
        return input_file.read()


class Database():
    database = []

    def __init__(self):
        pass

    def addEntry(self, entry: tuple):
        if len(entry) != 3:
            print('discarding entry, length not 3')

        self.database.append(entry)

    def entries(self):
        return self.database

    # TODO: refactor: unify the find word methods
    def findSecondWord(self, wordOne: str):
        foundEntries = [entry for entry in self.database if entry[0] == wordOne]

        if len(foundEntries) == 1:
            return foundEntries[0][1]

        return foundEntries[random.randrange(0, len(foundEntries))][1]
    
    def findNextWord(self, wordOne: str, wordTwo: str):
        foundEntries = [entry for entry in self.database if entry[0] == wordOne and entry[1] == wordTwo]

        if len(foundEntries) == 1:
            return foundEntries[0][2]

        return foundEntries[random.randrange(0, len(foundEntries))][2]


# Goes through the list of words, and stores them to the database
def processWords(words: str, database: Database):
    while len(words) > 2:
        entry = (words[0], words[1], words[2])
        database.addEntry(entry)

        del words[0]


if __name__ == "__main__":
    main()
