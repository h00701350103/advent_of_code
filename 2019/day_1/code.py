import requests
import os

def download_input(day=1):
    with open('../.cookie') as f:
        AUTH = f.read().strip()
    url = f"https://adventofcode.com/2019/day/{day}/input"
    cookies = dict(session=AUTH)
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.text
    else:
        print(r.status_code)

def get_input(day=1):
    if os.path.isfile('input.txt'):
        with open('input.txt') as f:
            return f.read()

    value = download_input(day)
    with open('input.txt', 'w') as f:
        f.write(value)
    return value

def clean_data(data):
    return [int(x) for x in data.split('\n') if x != '']

def star_one(masses):
    total = 0
    for mass in masses:
        total += add_fuel(mass)
    print(total)

def add_fuel(mass):
    fuel = (mass//3)-2
    if fuel <= 0:
        return 0
    return fuel + add_fuel(fuel)



if __name__ == '__main__':
    data = get_input()
    data = clean_data(data)
    star_one(data)
