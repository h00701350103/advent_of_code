import requests
import os

def download_input(day):
    with open('../.cookie') as f:
        AUTH = f.read()
    url = f"https://adventofcode.com/2019/day/{day}/input"
    cookies = dict(session=AUTH)
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.text
    else:
        print(r.status_code)

def get_input(day):
    if os.path.isfile('input.txt'):
        with open('input.txt') as f:
            return f.read()

    value = download_input(day)
    with open('input.txt', 'w') as f:
        f.write(value)
    return value

def clean_data(data):
    wires = data.split('\n')[:-1]
    wire_0 = [(x[0], int(x[1:])) for x in wires[0].split(',') if x != '']
    wire_1 = [(x[0], int(x[1:])) for x in wires[1].split(',') if x != '']
    return (wire_0, wire_1)

def move(origin, direction):
    result = origin
    if direction == 'U':
        result = (origin[0], origin[1] + 1)
    elif direction == 'D':
        result = (origin[0], origin[1] - 1)
    elif direction == 'L':
        result = (origin[0] - 1, origin[1])
    elif direction == 'R':
        result = (origin[0] + 1, origin[1])
    return result

def star_one(wires):
    board = {}
    location = (0, 0)
    for step in wires[0]:
        for i in range(step[1]):
            location = move(location, step[0])
            board[location] = 0

    best_distance = -1
    location = (0, 0)
    for step in wires[1]:
        for i in range(step[1]):
            location = move(location, step[0])
            if location in board:
                distance = abs(location[0]) + abs(location[1])
                if best_distance == -1 or distance < best_distance:
                    best_distance = distance

    print(best_distance)

def star_two(wires):
    board = {}
    location = (0, 0)
    time = 0
    for step in wires[0]:
        for i in range(step[1]):
            time += 1
            location = move(location, step[0])
            if location not in board:
                board[location] = time

    best_distance = -1
    location = (0, 0)
    time = 0
    for step in wires[1]:
        for i in range(step[1]):
            location = move(location, step[0])
            time += 1
            if location in board:
                distance = board[location] + time
                if best_distance == -1 or distance < best_distance:
                    best_distance = distance

    print(best_distance)


if __name__ == '__main__':
    day = int(os.path.dirname(os.path.realpath(__file__))[-1])
    data = get_input(day)
    data = clean_data(data)
    star_two(data)


