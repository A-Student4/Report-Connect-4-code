"""
https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf
A game of connect-4 Versus the computer
Author: Oscar A. Nieves
Updated: August 9, 2021
"""
from random import randint


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
def move(piece, board, Stacks, computer):
    Set0 = {'1', '2', '3', '4', '5', '6', '7'}
    if piece == computer:
        pos = randint(1, 7)
        if len(Stacks[pos - 1]) < 6:
            Stacks[pos - 1].push(piece)
            board[6 - len(Stacks[pos - 1])][pos - 1] = \
                Stacks[pos - 1].peek()
        else:
            move(piece, board, Stacks, computer)

    else:
        pos = 4
        if len(Stacks[pos - 1]) < 6:
            Stacks[pos - 1].push(piece)
            board[6 - len(Stacks[pos - 1])][pos - 1] = \
                Stacks[pos - 1].peek()
        else:
            pos = randint (1,7)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                move(piece, board, Stacks, computer)
    return board, Stacks


# Check wins -  adjusted so it put in a leaderboard ref: https://stackoverflow.com/questions/52448004/leaderboard-from-text-file-in-python
def checkWin(S, board):
    game = False
    # Horizontal checker
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
        file.close()
    return game
# https://www.w3schools.com/python/python_file_write.asp

# Main program -reference to the while true learnt:https://stackoverflow.com/a/36018439
while True:
    def main():
        # Prompt player input - change made: no longer asks for user input
        player1 ='X'
        computer1 = '0'

        # Print board
        board = initBoard()
        Stacks = initStacks()
        printBoard(board)
        game = False
        while game == False:
            # X player
            board, Stacks = move('X', board, Stacks, computer1)
            printBoard(board)
            game = checkWin('X', board)
            if game == True:
                break
            # O player
            board, Stacks = move('O', board, Stacks, computer1)
            printBoard(board)
            game = checkWin('O', board)
            if game == True:
                break
        print('Good game.')


    #https://stackoverflow.com/a/36018657 - showing me how to use repeat interations
    if __name__ == '__main__':
        main()
