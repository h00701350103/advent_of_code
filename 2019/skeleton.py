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
    return [int(x) for x in data.split(',') if x != '']


if __name__ == '__main__':
    data = get_input(2)
    data = clean_data(data)
    star_two(data)


