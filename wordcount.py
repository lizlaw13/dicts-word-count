# put your code here.
def word_counter(filename):
    file_name = open(filename)

    word_count = {}
    for line in file_name:
        line= line.rstrip()
        words = line.split(' ')
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f'{word} {count}')
    
word_counter('test.txt')
word_counter('twain.txt')
