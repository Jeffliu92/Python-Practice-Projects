#Write a function that takes a sentence and returns a dictionary with each word and how many times it appears.
def word_counting(sentence):
    empty_dict = {}
    words = sentence.lower().split()
    for word in words:
        if word not in empty_dict:
            empty_dict[word] = 1
        else:
            empty_dict[word] += 1

    return empty_dict

print(word_counting("Hello World Hello"))
