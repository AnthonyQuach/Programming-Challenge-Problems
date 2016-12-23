import queue
import copy

input_file = open("kermit_input.txt", 'r')


def is_valid(arrangement):  # function to check if a tile arrangement has no white tiles between black tiles
    state = ''
    for tile in arrangement:
        if state == '' and tile == 'B':
            state = 'B'
        elif state == 'B' and tile == 'W':
            state = 'BW'
        elif state == 'BW' and tile == 'B':
            return False
    return True


def swap(the_list, index_1, index_2):
    temp = the_list[index_1]
    the_list[index_1] = the_list[index_2]
    the_list[index_2] = temp
    return the_list


def flip(the_list, index):
    color = the_list[index]
    the_list[index] = 'W' if color == 'B' else 'B'
    return the_list


def possible_moves(arrangement):  # function to generate all 4 possible moves from a given tile arrangement
    moves = []
    frog_pos = arrangement.index('F')
    if frog_pos > 0:
        moves.append(swap(copy.deepcopy(arrangement), frog_pos, frog_pos - 1))
    if frog_pos < len(arrangement) - 2:
        moves.append(swap(copy.deepcopy(arrangement), frog_pos, frog_pos + 1))
    if frog_pos > 1:
        moves.append(flip(swap(copy.deepcopy(arrangement), frog_pos, frog_pos - 2), frog_pos))
    if frog_pos < len(arrangement) - 3:
        moves.append(flip(swap(copy.deepcopy(arrangement), frog_pos, frog_pos + 2), frog_pos))
    for move in moves:
        move[-1] += 1
    return moves


to_be_checked = queue.Queue()
line_num = 0
for line in input_file:
    line_num += 1
    tiles = list(line.strip())
    tiles.append(0)
    to_be_checked.queue.clear()
    to_be_checked.put(tiles)
    already_checked = {}
    while not to_be_checked.empty():
        check_now = to_be_checked.get()
        check_now_str = ''.join(check_now[0:len(check_now) - 1])
        if check_now_str in already_checked:
            continue
        already_checked[check_now_str] = 1
        if check_now[-1] == 10:
            print(str(line_num) + '. -1')
            break
        if is_valid(check_now):
            print(str(line_num) + '. ' + str(check_now[-1]))
            break
        for move in possible_moves(check_now):
            to_be_checked.put(move)



