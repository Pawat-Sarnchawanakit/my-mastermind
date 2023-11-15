import random

random.seed()


class Clue:

    def __init__(self, correctPos, correctColors, isSolved):
        self.__correctPos, self.__correctColors, self.__isSolved = correctPos, correctColors, isSolved

    def isSolved(self):
        return self.__isSolved

    def asString(self):
        return '*' * self.__correctPos + 'o' * self.__correctColors


class Board:

    def __init__(self, size, colors):
        self.__nColors = colors
        self.__nPositions = size

    def getSize(self):
        return self.__nPositions

    def getNumOfColors(self):
        return self.__nColors

    def initRandom(self):
        self.__board = tuple(
            random.randint(1, nColors) for x in range(nPositions))
        self.__boardSet = frozenset(self.__board)

    def isGuessValid(self, guess):
        if (len(guess) != self.__nPositions):
            return False
        zeroOrd = ord('0')
        maxOrd = zeroOrd + nColors
        for ch in guess:
            chOrd = ord(ch)
            if (chOrd <= zeroOrd or chOrd > zeroOrd + nColors):
                return False
        return True

    def getClue(self, guess):
        nCorrectPos = 0
        nCorrectColor = 0
        idx = 0
        zeroOrd = ord('0')
        for ch in guess:
            val = ord(ch) - zeroOrd
            if val == self.__board[idx]:
                nCorrectPos += 1
            elif val in self.__boardSet:
                nCorrectColor += 1
            idx += 1
        return Clue(nCorrectPos, nCorrectColor,
                    nCorrectPos == self.__nPositions)


board = Board(random.randint(1, 10), random.randint(1, 8))
board.initRandom()
rounds = 0
print(
    f"Playing Mastermind with {board.getNumOfColors()} colors and {board.getSize()} positions"
)
while True:
    guess = input("What is your guess?: ")
    if not board.isGuessValid(guess):
        print("Bad guess.\nTry again.")
        continue
    print(f"Your guess is {guess}")
    rounds += 1
    clue = board.getClue(guess)
    print(clue.asString())
    if clue.isSolved():
        break
print(f"You solved it after {rounds} rounds.")
