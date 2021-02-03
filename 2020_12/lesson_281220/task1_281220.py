# task1_281220
'''
Task 1
Make a program that has some sentence (a string) on input and returns a dict
containing all unique words as keys and the number of occurrences as values.
'''
split_sentence = input('Input the sentence: ').split()
dict_words = {}
for i in split_sentence:
    dict_words[i] = split_sentence.count(i)
print(dict_words)


