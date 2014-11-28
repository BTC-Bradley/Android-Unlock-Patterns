__author__ = 'hanso_000'

import itertools


def get_intermediate(pair):
    intermediates = {
        '1': [['0', '2'], ['2', '0']],
        '3': [['0', '6'], ['6', '0']],
        '4': [['3', '5'], ['5', '3'], ['1', '7'], ['7', '1'], ['0', '8'], ['8', '0'], ['2', '6'], ['6', '2']],
        '5': [['2', '8'], ['8', '2']],
        '7': [['6', '8'], ['8', '6']]
    }
    for key in intermediates:
        if pair in intermediates[key]:
            return key


def build_codes():
    # Dictionary that lists what nodes are valid moves with given node/key
    valid_moves = {
        '0': {'1', '3', '4', '5', '7'},
        '1': {'0', '2', '3', '4', '5', '6', '8'},
        '2': {'1', '3', '4', '5', '7'},
        '3': {'0', '1', '2', '4', '6', '7', '8'},
        '4': {'0', '1', '2', '3', '5', '6', '7', '8'},
        '5': {'0', '1', '2', '4', '6', '7', '8'},
        '6': {'1', '3', '4', '5', '7'},
        '7': {'0', '2', '3', '4', '5', '6', '8'},
        '8': {'1', '3', '4', '5', '7'}
    }

    jumps = {
        '0': {'2', '6', '8'},
        '1': {'7'},
        '2': {'0', '6', '8'},
        '3': {'5'},
        '4': {},
        '5': {'3'},
        '6': {'0', '2', '8'},
        '7': {'1'},
        '8': {'0', '2', '6'}
    }

    gross = list()

    # Gross is a list of lists of all the permutations of all 9 nodes of each len(4,5,6,7,8,9)
    for i in range(4, 10):
        gross.append(list((itertools.permutations('012345678', i))))

    pruned = list()

    # Remove permutations from gross that are not valid to create net
    for perm in gross:

        temp = list()

        # Gets each individual code from the list of permutations
        for code in perm:
            valid_move = True
            been_visited = {
                '0': False,
                '1': False,
                '2': False,
                '3': False,
                '4': False,
                '5': False,
                '6': False,
                '7': False,
                '8': False,
            }
            # Gets each node in the code and checks it with the next node to see if it is valid using the dictionary
            for k in range(len(code) - 1):
                node = code[k]
                been_visited[node] = True
                next_node = code[k + 1]

                pair = list()
                pair.append(node)
                pair.append(next_node)

                special_case = False
                inter = get_intermediate(pair)

                if next_node in jumps[node] and been_visited[inter]:
                    special_case = True

                # If if k to k+1 is not a valid move, flag the given code
                if next_node not in valid_moves[node] and not special_case:
                    valid_move = False

            # temp ends up being a complete list of all the valid codes at the given len
            if valid_move:
                temp.append(code)
        # pruned ends up being a list of lists that contain all the valid codes by len pruned[0] = len 3
        pruned.append(temp)
    return pruned


class Node():
    def __init__(self):
        self.value = -1
        self.parent = None

        self.zero = None
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.seven = None
        self.eight = None

        self.valid_code = False


def build_tree(codes):
    parent = Node()
    #for i in range(0,)



def fill_tree(codes):
    pass


def main():

    codes = build_codes()
    f = open('codes.txt', 'w')

    for givenLenCode in codes:
        for code in givenLenCode:
            temp = ''
            for numb in code:
                temp += numb
            f.write(temp + '\n')

    f.close()

    #tree = build_tree(codes)



main()