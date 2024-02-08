from string import ascii_letters
def own_dictionary(to_dict, sentence):
    dictionary, char, total = {}, ord("a"), ""
    for new_value in to_dict:
        dictionary.setdefault(chr(char), new_value)
        char += 1
    for char in sentence:
        if char.lower() in dictionary:
            total += dictionary[char.lower()]
        else:
            total += char
    return total

def faster(to_dict, in_sent):
    translator = str.maketrans(ascii_letters, to_dict * 2)
    return in_sent.translate(translator)