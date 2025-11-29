from random import randint

#Results for when player 1 places it in the middle and then player 2 places on top until it is full! (No draws analysed!)






# Class stack (for each column)
class Stack:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return

    def peek(self):
        return self._list[-1]




# Initialize board (empty)
def initBoard():
    # empty board
    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    board = []
    for i in range(0, len(rows)):
        board.append([' '] * 7)

    return board


# Initialize Stacks (empty
def initStacks():
    S = [Stack(), Stack(), Stack(),
         Stack(), Stack(), Stack(), Stack()]
    return S


# print board
def printBoard(board):
    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    top = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0, 7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-' * (len(top) - 3))
    for j in range(0, len(rows)):
        for i in range(1, 8):
            row[j][0] = row[j][0] + str(board[j][i - 1]) + ' | '
        print(row[j][0])
        print('  ' + '-' * ((len(row[j][0]) - 3)))
    print(top)
    print('')


# Move - i am going to need to change this so i can the player 1 input as random and the first move to always be 1
# ok so i have got rid of the input and now the it is plays a random game now i need to make it so that player always plays it in column 4 first and then store data and graph it!
#adjusted the "stacks[pos-1]<1 part:" ADDed
def move(piece, board, Stacks, computer):
    Set0 = {'1', '2', '3', '4', '5', '6', '7'}

    if piece == computer:
        pos = 7
        if len(Stacks[pos - 1]) < 1:
            Stacks[pos - 1].push(piece)
            board[6 - len(Stacks[pos - 1])][pos - 1] = \
                Stacks[pos - 1].peek()
        else:
            pos = randint(1, 7)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                move(piece, board, Stacks, computer)

    if computer != piece:
        pos = 4
        if len(Stacks[pos - 1]) < 1:
            Stacks[pos - 1].push(piece)
            board[6 - len(Stacks[pos - 1])][pos - 1] = \
                Stacks[pos - 1].peek()
        else:
            pos = randint(1,7)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                move(piece, board, Stacks, computer)
    return board, Stacks







# Check wins -  adjusted so it put in a leaderboard ref
def checkWin(S, board):
    game = False
    # Horizontal checker - j seems to be no of rows and i is no of columns
    for j in range(0, 6):
        for i in range(3, 7):
            if (board[j][i] == board[j][i - 1] == \
                    board[j][i - 2] == board[j][i - 3] == S):
                game = True
            else:
                continue
                # Vertical checker
    for i in range(0, 7):
        for j in range(3, 6):
            if (board[j][i] == board[j - 1][i] == \
                    board[j - 2][i] == board[j - 3][i] == S):
                game = True
            else:
                continue
    # Diagonal checker
    for i in range(0, 4):
        for j in range(0, 3):
            if (board[j][i] == board[j + 1][i + 1] == \
                    board[j + 2][i + 2] == board[j + 3][i + 3] == S or
                    board[j + 3][i] == board[j + 2][i + 1] == \
                    board[j + 1][i + 2] == board[j][i + 3] == S):
                game = True
            else:
                continue
    if game == True:
        print(S + ' wins!')
        file = open("Leaderboard.txt", "a")
        file.write(S + "\n")
        file.close
    return game
# Main program -reference to the while true learnt:https://stackoverflow.com/a/36018439
while True:
    def main():
        # Prompt player input - change made: no longer asks for user input
        player1 ='X7'
        computer1 = 'O7'

        # Print board
        board = initBoard()
        Stacks = initStacks()
        printBoard(board)
        game = False
        while game == False:
            # X player
            board, Stacks = move('X7', board, Stacks, computer1,)
            printBoard(board)
            game = checkWin('X7', board)

            if game == True:
                break
            # O player
            board, Stacks = move('O7', board, Stacks, computer1,)
            printBoard(board)
            game = checkWin('O7', board)
            if game == True:
                break

        print('Good game.')



    if __name__ == '__main__':
        main()