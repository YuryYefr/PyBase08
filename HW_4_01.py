from string import ascii_letters, digits, whitespace, punctuation


def clear_word(word, filterstr):
    result = ""
    for element in word.split():
        if element not in filterstr:
            result = word.replace(element, "")
    for element in word[::]:
        if element not in filterstr:
            raise ValueError(word.index(element))

    return result


if __name__ == "__main__":
    word = "\tShakespeare's sonnets are poems" \
           "\n that William Shakespeare wrote on a variety of themes." \
 \
           "\n When discussing or referring to Shakespeare’s sonnets, it is almost always a reference to the 154 sonnets"
    filterstr = ascii_letters, digits, whitespace, punctuation
    res = clear_word(word, filterstr)
    print(res)
