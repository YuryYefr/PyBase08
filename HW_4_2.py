from string import whitespace, punctuation, digits, ascii_letters


def check(element, filterstr):
    for i in element:
        if i not in filterstr:
            return False
    return True


def get_eng_words(text, filterstr):
    result = set([])
    for element in text.split():
        if check(element, filterstr):
            result.add(element)

    return result


if __name__ == "__main__":
    TEXT = "Shakespeare's sonnets are poems" \
           " that William Shakespeare wrote onа a variety of themes." \
 \
           " When discussing or referring to Shakespeare’s sonnets, it is almost always a reference to the 154 sonnets"
    filterstr = ascii_letters + digits + whitespace + punctuation
    print(get_eng_words(TEXT, filterstr))
