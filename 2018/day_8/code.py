


def star_1(filename='input.txt'):
    with open(filename) as f:
        number_list = [int(i) for i in f.readline().split(' ')]
        pass
    print(parse_node_1(number_list, 0))

def star_2(filename='input.txt'):
    with open(filename) as f:
        number_list = [int(i) for i in f.readline().split(' ')]
        pass
    print(parse_node_2(number_list, 0))

def parse_node_1(number_list, index):
    child_count = number_list[index]
    meta_count = number_list[index+1]
    index += 2
    total = 0

    for i in range(child_count):
        res, index = parse_node_1(number_list, index)
        total += res

    for meta in number_list[index:index+meta_count]:
        total += meta
    index += meta_count

    return total, index

def parse_node_2(number_list, index):
    child_values = [0] * number_list[index]
    meta_count = number_list[index+1]
    index += 2

    if len(child_values) == 0:
        return sum(number_list[index : index+meta_count]), index+meta_count


    for i in range(len(child_values)):
        child_values[i], index = parse_node_2(number_list, index)

    total = 0
    for meta in number_list[index:index+meta_count]:
        total += 0 if meta > len(child_values) else child_values[meta-1]


    return total, index+meta_count

if __name__ == '__main__':
    #star_1()
    star_2()


