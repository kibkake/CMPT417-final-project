import json
import time
from copy import deepcopy

from Puzzle import FifteenPuzzle
import random

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


def getPossibleMoves(state):
    pos = state.index(0)

    if pos == 0:
        possible_moves = [1, 4]
    elif pos == 1:
        possible_moves = [1, 4, -1]
    elif pos == 2:
        possible_moves = [4, -1, 1]
    elif pos == 3:
        possible_moves = [-1, 4]
    elif pos == 4:
        possible_moves = [-4, 4, 1]
    elif pos == 7:
        possible_moves = [-4, 4, -1]
    elif pos == 8:
        possible_moves = [1, -4, 4]
    elif pos == 11:
        possible_moves = [-1, 4, -4]
    elif pos == 12:
        possible_moves = [-4, 1]
    elif pos == 13:
        possible_moves = [1, -1, -4]
    elif pos == 14:
        possible_moves = [1, -1, -4]
    elif pos == 15:
        possible_moves = [-4, -1]
    else:
        possible_moves = [-4, 1, 4, -1]

    return possible_moves


def applyMove(state, direction):
    next_state = deepcopy(state)
    pos = state.index(0)
    # Position blank tile will move to.
    next_pos = pos + direction
    # Swap tiles.
    next_state[pos], next_state[next_pos] = next_state[next_pos], next_state[pos]
    return next_state


def generate_puzzle(goal=None, num=10, moves=5):
    if goal is None:
        goal = goal_state
    generated = []
    for i in range(num):
        state = goal
        for j in range(moves):
            possible_move = getPossibleMoves(state)
            rand_move = random.sample(possible_move, 1)[0]
            state = applyMove(state, rand_move)
        puzzle = FifteenPuzzle(state)
        if puzzle.check_solvability(puzzle.initial):
            generated.append(tuple(puzzle.initial))
        else:
            num += 1

    with open("generated15.txt", "w") as f:
        for puzzle in generated:
            f.write(str(puzzle))
            f.write("\n")


if __name__ == "__main__":
    start_time = time.time()
    generate_puzzle(goal_state, 5000, 20)
    elapsed_time = time.time() - start_time
    print("done generating tests...")
    print(f'elapsed time (in seconds): {elapsed_time}s')
