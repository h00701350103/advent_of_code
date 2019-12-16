import requests
import os

def download_input(day):
    with open('../.cookie') as f:
        AUTH = f.read().strip()

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
    return [int(x) for x in data.split(',') if x != '']

def star_one(program):
    PC = 0
    while PC < len(program):
        instruction = program[PC]
        if instruction == 99:
            return program[0]
        elif instruction == 1:
            program[program[PC+3]] = program[program[PC+1]] + program[program[PC+2]]
        elif instruction == 2:
            program[program[PC+3]] = program[program[PC+1]] * program[program[PC+2]]
        else:
            raise RuntimeError('Unknown instruction')
        PC += 4
    raise RuntimeError('Program exited incorrectly')


def star_two(program):
    for noun in range(10000):
        print(noun)
        for verb in range(100):
            data = program.copy()
            data[1] = noun
            data[2] = verb
            try:
                if star_one(data) == 19690720:
                    print(noun, verb)
                    return
            except IndexError:
                continue


if __name__ == '__main__':
    data = get_input(2)
    data = clean_data(data)
    star_two(data)


