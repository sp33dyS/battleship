# -*- coding: utf-8 -*-
"""
Battleship! game from Codecademy Python tutorial.
Version: 0.1
Created on Wed Mar 28 01:03:56 2018

@author: sp33dy
"""
from random import randint

board = []
turn = 0
shots = []

for x in range(7):
    board.append(["O"] * 7)


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
ship2_row = random_row(board)
ship2_row != ship_row
ship2_col = random_col(board)
ship2_col != ship_col

# print("First ship:", ship_row, ship_col)
# print("Second ship:", ship2_row, ship2_col, "\n")
print("Welcome to battleship game.\nA ship's size is only one character")
print("Try to guess rows and columns from 0 to 6.")
print("\nThere are ten turns and two ships. Good luck!")

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(1, 11):
    print("\nTurn", turn)

    guess_row = int(input("Guess row: "))
    guess_col = int(input("Guess col: "))

    if len(shots) == 1:
        print()
        board[guess_row][guess_col] = "X"
        print_board(board)
        print("\nWINNER!!!")
        break
    elif guess_row == ship_row and guess_col == ship_col:
        print("\nCongratulations! You sunk my first battleship!\n")
        board[guess_row][guess_col] = "X"
        print_board(board)
        shots.append(1)
    elif guess_row == ship2_row and guess_col == ship2_col:
        print("\nCongratulations! You sunk my second battleship!\n")
        board[guess_row][guess_col] = "X"
        print_board(board)
        shots.append(2)
    else:
        if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
            print("\nOops, that's not even in the ocean.\n")
        elif (board[guess_row][guess_col] == "-"):
            print("\nYou guessed that one already.\n")
            print_board(board)
        else:
            print("\nYou missed my battleship!\n")
            board[guess_row][guess_col] = "-"
            if turn == 10:
                print("\nGame Over")
                print("First ship was at row", ship_row, "and column", ship_col)
                print("Second ship was at row", ship2_row, "and column", ship2_col, "\n")
                board[ship_row][ship_col] = "X"
                board[ship2_row][ship2_col] = "X"
            print_board(board)
