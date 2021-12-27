import re
from math import inf
from pathlib import Path
from functools import lru_cache
path = Path.cwd() / 'input' / 'day23.txt'
data = open(path).read().strip().split('\n')

# Set Point index
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
# ['#',  0 ,  1 , '.',  2 , '.',  3 , '.',  4 ,  ',', 5 ,  6 , '#']  --- > hallway
# ['#', '#', '#',  0 , '#',  1 , '#',  2 , '#',  3 , '#', '#', '#']  
# ['#', '#', '#',  0 , '#',  1 , '#',  2 , '#',  3 , '#', '#', '#']  --- > rooms 
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']

hallway = (None, ) * 7
rooms = []
for species in zip(re.findall('\w', data[2]), re.findall('\w', data[3])):
    rooms.append(tuple(map('ABCD'.index, species)))
rooms = tuple(rooms)

ROOM_DISTANCE = (
	(2, 1, 1, 3, 5, 7, 8), # from/to room 0
	(4, 3, 1, 1, 3, 5, 6), # from/to room 1
	(6, 5, 3, 1, 1, 3, 4), # from/to room 2
	(8, 7, 5, 3, 1, 1, 2), # from/to room 3
)

# hallway spots:  0 | 1 | 2 | 3 | 4 | 5 | 6
#                       ^   ^   ^   ^
# rooms:                0   1   2   3
def cal_cost(room, hallway, r, h , room_size, to_room = False): 
    if r + 1 < h :
        start = r + 2
        end = h + (not to_room) # if hallway -> room hallway[end] is fill with amphipods, so ignore end point
    else:
        start = h + to_room # if hallway -> room hallway[start] is fill with amphipods, so ignore start point
        end = r + 2
    for x in hallway[start:end]:
        if x != None : return inf
    target = hallway[h] if to_room else room[0]
    return 10**target * (ROOM_DISTANCE[r][h] + (to_room - len(room) + room_size))


def move_in(rooms, hallway, room_size):
    for h_idx, val in enumerate(hallway):
        if val == None : continue

        room = rooms[val]
        if any(s != val for s in room): continue

        cost = cal_cost(room, hallway, val, h_idx, room_size, to_room = True)
        if cost == inf : continue
        new_rooms = rooms[:val] + ((val,) + room,) + rooms[val + 1:]
        new_hallway = hallway[:h_idx] + (None,) + hallway[h_idx + 1:]
        yield cost, (new_rooms, new_hallway)


def move_out(rooms, hallway, room_size):
    for r_idx, room in enumerate(rooms):
        if all(s == r_idx for s in room): continue

        for h_idx in range(7):
            cost = cal_cost(room, hallway, r_idx, h_idx, room_size)
            if cost == inf : continue

            new_rooms   = rooms[:r_idx] + (room[1:],) + rooms[r_idx + 1:]
            new_hallway = hallway[:h_idx] + (room[0],) + hallway[h_idx + 1:]
            yield cost, (new_rooms, new_hallway)


def possible_moves(rooms, hallway, room_size):
    yield from move_in(rooms, hallway, room_size)
    yield from move_out(rooms, hallway, room_size)


def check(rooms, room_size):
    for r_idx, room in enumerate(rooms):
        if len(room) != room_size or any(s != r_idx for s in room):
            return False
    return True

@lru_cache(maxsize=None)
def solution(rooms, hallway, room_size):
    if check(rooms, room_size): return 0

    answer = inf
    for cost, next_state in possible_moves(rooms, hallway, room_size):
        cost += solution(*next_state, room_size)
        if cost < answer :
            answer = cost
    return answer


answer_p1 = solution(rooms, hallway, 2)
print(answer_p1)
print('-'*30)


rooms_p2 = []
for room, new in zip(rooms, [(3, 3), (2, 1), (1, 0), (0, 2)]):
	rooms_p2.append((room[0], *new, room[-1]))

rooms_p2 = tuple(rooms_p2)
answer_p2 = solution(rooms_p2, hallway, 4)
print(answer_p2)