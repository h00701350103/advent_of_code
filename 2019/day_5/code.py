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

def both_stars(program, data_input=1):
    def get_value(mode, param):
        if mode % 10 == 0:
            return program[param]
        if mode % 10 == 1:
            return param

    PC = 0
    while PC < len(program):
        instruction = program[PC] % 100
        param_modes = program[PC] // 100

        if instruction == 99:
            return program[0]
        elif instruction == 1:
            program[program[PC+3]] = (
                get_value(param_modes, program[PC+1])
                + get_value(param_modes//10, program[PC+2]))
            PC += 4
        elif instruction == 2:
            program[program[PC+3]] = (
                get_value(param_modes, program[PC+1])
                * get_value(param_modes//10, program[PC+2]))
            PC += 4
        elif instruction == 3:
            program[program[PC+1]] = data_input # input()
            PC += 2
        elif instruction == 4:
            print(get_value(param_modes, program[PC+1]))
            PC += 2
        elif instruction == 5:
            if get_value(param_modes, program[PC+1]):
                PC = get_value(param_modes//10, program[PC+2])
            else:
                PC += 3
        elif instruction == 6:
            if not get_value(param_modes, program[PC+1]):
                PC = get_value(param_modes//10, program[PC+2])
            else:
                PC += 3
        elif instruction == 7:
            program[program[PC+3]] = int(
                get_value(param_modes, program[PC+1]) <
                get_value(param_modes//10, program[PC+2]))
            PC += 4
        elif instruction == 8:
            program[program[PC+3]] = int(
                get_value(param_modes, program[PC+1]) ==
                get_value(param_modes//10, program[PC+2]))
            PC += 4

        else:
            raise RuntimeError('Unknown instruction {} at addr {}'.format(
                instruction, PC))
    raise RuntimeError('Program exited incorrectly')


if __name__ == '__main__':
    data = get_input(5)
    data = clean_data(data)
    both_stars(data, 5)


