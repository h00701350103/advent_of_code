guards_time_slept = {}
fav_time_slept = {}

with open("sorted_input_1.txt") as f:
    lines = f.readlines()

i = 0

while i < len(lines):
    guard = int(lines[i].split(" ")[3][1:])
    if guard not in guards_time_slept:
        guards_time_slept[guard] = 0
        fav_time_slept[guard] = [0] * 60
    i += 1
    while i < len(lines) and "Guard" not in lines[i]:
        asleep = int(lines[i][15:17])
        i += 1
        awake =  int(lines[i][15:17])
        guards_time_slept[guard] += awake-asleep
        i += 1
        for j in range(asleep, awake):
            fav_time_slept[guard][j] += 1
        #if guard == 499:
            #print(asleep, awake)
            #print(fav_time_slept[499])

print(guards_time_slept)

max_time = 0
max_guard = -1
for guard, time_list in fav_time_slept.items():
    for i in range(len(time_list)):
        if time_list[i] > max_time:
            max_guard = guard
            max_time = time_list[i]
            max_minute = i
#print(max_guard, max_time, fav_time_slept[max_guard],
      #fav_time_slept[max_guard].index(max(fav_time_slept[max_guard])))
print(max_guard, max_time, max_minute, max_guard*max_minute)


