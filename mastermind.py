import random;
random.seed();
nColors = random.randint(1, 8)
nPositions = random.randint(1, 10)

def isInputValid(inp):
    if(len(inp) != nPositions):
        return False;
    for ch in inp:
        if(ord(ch) <= ord('0') or ord(ch) > ord('0')+nColors):
            return False;
    return True;

board = tuple(random.randint(1, nColors) for x in range(nPositions));
boardSet = frozenset(board);
rounds=0;
print(f"Playing Mastermind with {nColors} colors and {nPositions} positions");
while True:
    guess = input("What is your guess?: ");
    if not isInputValid(guess):
        print("Bad guess.\nTry again.");
        continue;
    print(f"Your guess is {guess}");
    cp = 0;
    cc = 0;
    i = 0;
    for ch in guess:
        val = ord(ch)-ord('0');
        if val == board[i]:
            cp += 1;
        elif val in boardSet:
            cc += 1;
        i += 1;
    print('*'*cp + 'o'*cc)
    rounds += 1;
    if cp == nPositions:
        break;
print(f"You solved it after {rounds} rounds.")
