import csv

length_word = 5

# Create csv file for each word length in the Lexicon
# Word in the Lexicon are ordered by length
with open('Lexicon_FR.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    writer = csv.writer(open(f'mot_{length_word}.csv', 'w', newline=''))
    for row in csv_reader:
        if len(row[0]) == length_word:
            writer.writerow(row)
        else:
            length_word += 1
            print(f'New file mot_{length_word}.csv')
            writer = csv.writer(open(f'mot_{length_word}.csv', 'w', newline=''))
            writer.writerow(row)

        print(f'\t{row[0]}')
        line_count += 1
    
    print(f'Processed {line_count} lines.')