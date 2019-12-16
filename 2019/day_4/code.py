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


def star_one(data):
    def validate_password(password):
        digits = str(password)

        adjacent_digits = False
        for i in range(len(digits)-1):
            if digits[i] > digits[i+1]:
                return False
            if digits[i] == digits[i+1]:
                adjacent_digits = True

        return adjacent_digits

    result = 0
    for password in data:
        if validate_password(password):
            result += 1
    return result


def star_two(data):
    def validate_password(password):
        digits = str(password)

        adjacent_digits = False
        banned_digit = ''

        for i in range(len(digits)-1):
            if digits[i] != banned_digit:
                banned_digit = ''

            if digits[i] > digits[i+1]:
                return False
            if digits[i] == digits[i+1]:
                if i < len(digits) - 2 and digits[i] == digits[i+2]:
                    banned_digit = digits[i]
                    continue

                if digits[i] != banned_digit:
                    adjacent_digits = True

        return adjacent_digits

    result = 0
    for password in data:
        if validate_password(password):
            result += 1
    return result





if __name__ == '__main__':
    #data = get_input(2)
    #data = clean_data(data)
    data = range(271973, 785961+1)
    print(star_two(data))


