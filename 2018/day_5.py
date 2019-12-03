def polymer_length(polymer):
    i = 0
    while i < len(polymer) - 1:
        left = polymer[i]
        right = polymer[i+1]
        if left.upper() == right.upper() and left != right:
            polymer = polymer[:i] + polymer[i+2:]
            i = max(0, i-1)
        else:
            i += 1
    return(len(polymer))

with open("input_5.txt") as f:
    polymer = f.readlines()[0][:-1]

polymer_dict={}
min_length = 999999999999999999
min_letter = ''
for letter in 'abcdefghijklmnopqrstuvwxyz':
    pruned_polymer = polymer.replace(letter, "").replace(letter.upper(), "")
    length = polymer_length(pruned_polymer)
    polymer_dict[letter] = length
    if length < min_length:
        min_length = length
        min_letter = letter


print(polymer_dict)
print(min_letter, min_length)
