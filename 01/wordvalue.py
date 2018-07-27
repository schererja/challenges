from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        lines = f.read().strip().splitlines()
    return lines

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_count = 0
    for letter in list(word):
        if (letter != '-'):
            word_count = word_count + LETTER_SCORES[letter.upper()]
    return word_count


def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if(words == None):
        words = load_words()
    return max(words, key=calc_word_value)


if __name__ == "__main__":
    pass # run unittests to validate
