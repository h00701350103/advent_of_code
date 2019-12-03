

def star_1(filename='input.txt'):
    with open(filename) as f:
        for line in f:
            players, last_marble = [int(i) for i in line.split(' ')]
            print(brute_high_score(players, last_marble))

def star_2(filename='input.txt'):
    with open(filename) as f:
        for line in f:
            players, last_marble = [int(i) for i in line.split(' ')]
            print(optimized_high_score(players, last_marble))


def brute_high_score(player_count, last_marble):
    circle = [0]
    players = [0] * player_count
    current_marble_index = 0

    for i in range(1, last_marble+1):
        #if current_marble_index + 2 > len(circle):
            #print(len(circle))
            #print(circle)
            #input()
        if i % 23 != 0:
            current_marble_index = (current_marble_index + 2 ) % len(circle)
            if current_marble_index == 0:
                current_marble_index = len(circle)
                circle.append(i)
            else:
                circle.insert(current_marble_index, i)
        else:
            current_player = (i - 1) % player_count
            current_marble_index = (current_marble_index - 7 ) % len(circle)
            #print(i-4, circle[current_marble_index])
            players[current_player] += i + circle.pop(current_marble_index)

    return max(players)

def high_score(player_count, last_marble):
    players = [0] * player_count
    removed_marbles = set()


    for i in range(23, last_marble+1, 23):
        current_player = (i - 1) % player_count

def optimized_high_score(player_count, last_marble):
    old_list = [0, 2, 1, 3]
    new_list = [0, 4, 2, 5, 1, 6]

    players = [0] * player_count
    old_list_marble_index = 2

    insert_cycle = [[i] for i in range(7-23, -5)]
    insert_cycle += [(-5, -4), None, (1, -3, 2), (3, -2, 4), (5, -1, 6)] #insert None

    for i in range(23, last_marble+1, 23):
        for j in insert_cycle:
            old_list_marble_index += 1
            if old_list_marble_index >= len(old_list):
                old_list = new_list
                new_list = []
                old_list_marble_index = 0

            if j == None:
                players[i % player_count] += i + old_list[old_list_marble_index]
                continue

            new_list.append(old_list[old_list_marble_index])
            new_list += [k + i for k in j]
    return max(players)



#def process_list(prev_list = [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 26, 21, 27, 5, 28, 22, 29,
#                              11, 30, 1, 31, 12, 32, 6, 33, 13, 34, 3, 35, 14, 36, 7, 37, 15, 38],
#                 curr_marble = 39, index = 1):
#
#    new_list = [0] * int(len(prev_list) * 2.4)
#    old_list_index = 0
#    new_list_index = 1

    ##if curr_marble % 23 is too big, we need to do the special wrap-around

    #start of 23
    ##loop until curr_marble % 23 == 23-5
        #copy old value
        #insert curr_marble
    ###or do a weirdo one-liner
    ###new_list[curr_marble : curr_marble + 18 - (curr_marble % 23] = 
    ###nah scratch that

    ##save old_list_index to the high score, increment by 1 skipping it
    ##add our multiple of 23 to the high score, hereby known as x
    #insert x-5, x-4, old_list_index, x+1, x-3, x+2, old_list_index, x+3, x-2, x+4, old_list_index,
    #x+5, x-1, x+6

    #goto start of 23, unless we're at the end of the list

     








if __name__ == '__main__':
    #star_1()
    star_2()
