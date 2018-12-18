from string import ascii_letters, digits, whitespace, punctuation


def clear_word(word, filterstr):
    result = ""
    for element in word:
        if element in filterstr:
            result += element

    return result


def checkword(word, filterstr):
    for element in word:
        if element not in filterstr:
            raise ValueError(word.index(element))


if __name__ == "__main__":
    word = "Shakespeare's sonnets are poems" \
           "\n that William Shakespeare wrote on a variety of themes." \
 \
           "\n When discussing or referring to Shakespeare’s sonnets, it is almost always a reference to the 154 sonnets"
    filterstr = ascii_letters + digits + whitespace + punctuation
    try:
        checkword(word, filterstr)
    except ValueError as e:
        print(e)
        print(clear_word(word, filterstr))
