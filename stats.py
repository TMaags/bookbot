def count_words(strings_to_count):
    words = strings_to_count.split()
    num_words = len(words)
    return num_words

def count_characters(string_to_count):
    characters_dict = {}
    characters_lowered = string_to_count.lower()

    for char in characters_lowered:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def sorted_characters(unsorted_dict):
    list_dict = []
    for char, count in unsorted_dict.items():
        if char.isalpha() == True:
            list_dict.append({char: count})
    list_dict.sort(key=lambda d: list(d.values())[0], reverse=True)
    return list_dict

