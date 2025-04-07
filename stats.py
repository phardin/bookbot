def get_num_words (text):
    return len(text.split())

def get_char_count (text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 0
        char_count[char.lower()] += 1
    return char_count

def get_sort_dicts (char_count):
    dicts = []
    for char, num in char_count.items():
        dicts.append({"char": char, "num": num})
    return dicts

def sort_on_count(dict):
    return dict["num"]