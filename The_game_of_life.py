# Game of life is a 0-player game, the function receive an input of a 2d numpy array
# of zeros and ones and go over its life till it reaches a stalemate state, operating in space complexity of O(1)
import numpy as np
import codecs, json
import sys

def curr_state(input):
    Row, Col = input.shape

    def num_adjacent(r, c):
        nums = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if ((i == r and j == c) or i < 0 or j < 0 or i >= Row or j >= Col):
                    continue
                elif input[i, j] in [1, 3]:
                    nums += 1
        return nums

    for r in range(Row):
        for c in range(Col):
            nums = num_adjacent(r, c)
            if input[r, c]:
                if nums in [2, 3]:
                    input[r, c] = 3
            elif nums == 3:
                input[r, c] = 2

    for r in range(Row):
        for c in range(Col):
            if input[r, c] == 1:
                input[r, c] = 0
            if input[r, c] in [2, 3]:
                input[r, c] = 1


def start(inputs, life_cycles):
    for cycle in range(life_cycles):
        old_state = np.copy(inputs)
        curr_state(inputs)
        if np.array_equal(inputs, old_state):
            print("end of life")
            print(inputs, "\n")
            break
        print(inputs," cycle = {}".format(cycle + 1) , "\n")


#reads a json file with 2D numpy array of ones and zeros
file_path = sys.path[0] + "/config2.json"
obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
b_new = json.loads(obj_text)
a_new = np.array(b_new)
life_cycles = 100

starter = start(a_new, life_cycles)

# state = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
# life_cycles_ = 10
