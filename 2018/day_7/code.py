


def star_1(filename):
    #requirements = [[] for i in range(25)]
    all_requirements = {}
    finished_steps = ''
    remaining = []
    with open(filename) as f:
        for line in f:
            requirement, step = [line.split()[i] for i in (1, 7)]
            if step not in all_requirements:
                all_requirements[step] = []

            all_requirements[step].append(requirement)
            if step not in remaining:
                remaining.append(step)
            if requirement not in remaining:
                remaining.append(requirement)

    remaining.sort()
    while remaining:
        for step in remaining:
            all_done = True
            if step in all_requirements:
                for requirement in all_requirements[step]:
                    if requirement in remaining:
                        all_done = False
                        break
            if all_done:
                remaining.remove(step)
                finished_steps += step
                break
    print(finished_steps)

def star_2(filename, base_time, workers):
    #requirements = [[] for i in range(25)]
    all_requirements = {}
    finished_steps = ''
    remaining = []
    with open(filename) as f:
        for line in f:
            requirement, step = [line.split()[i] for i in (1, 7)]
            if step not in all_requirements:
                all_requirements[step] = []

            all_requirements[step].append(requirement)
            if step not in remaining:
                remaining.append(step)
            if requirement not in remaining:
                remaining.append(requirement)

    remaining.sort()
    in_progress = {}
    time = -1
    while remaining or in_progress:
        available = []
        time += 1
        
        done = []
        for i in in_progress:
            in_progress[i] -= 1
            if in_progress[i] == 0:
                done.append(i)
        if not done and in_progress:
            continue
        for i in done:
            finished_steps += i
            in_progress.pop(i)


            

        for step in remaining:
            all_done = True
            if step in all_requirements:
                for requirement in all_requirements[step]:
                    if requirement in remaining or requirement in in_progress:
                        all_done = False
                        break
            if all_done:
                available.append(step)
        while len(in_progress) < workers and available:
            step = available.pop(0)
            remaining.remove(step)
            in_progress[step] = base_time + ord(step) - ord('A') + 1
    print(finished_steps, time)

if __name__ == '__main__':
    star_2('example.txt', 0, 2)
    #star_2('input.txt', 60, 4)



