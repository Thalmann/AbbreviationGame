
abbreviations = list()

with open('../raw_data/basic_computer_abbreviations.txt', 'r') as f:
    for line in f:
        abbreviations.append(line.split('—'))


with open('../database/basic_computer_abbreviations.txt', 'w') as f:
    for item in abbreviations:
        f.write(','.join(item))
