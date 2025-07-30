def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    word_counter = 0
    tot_word_list = file_contents.split()
    for i in range(0, len(tot_word_list)):
        word_counter += 1
    return word_counter

def letter_counter(file_contents):
    letter_dict = {}
    tot_word_list = file_contents.lower()

    for char in tot_word_list:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def sort_on(items):
    return items["num"]

def sort_dict(letter_dict):
    my_list = []
    for i in letter_dict:
        if i.isalpha():
            placeholder = {"char": i, "num": letter_dict[i]}
            my_list.append(placeholder)
    my_list.sort(reverse=True, key=sort_on)
    return my_list
    