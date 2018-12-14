from string import whitespace, punctuation


def get_vocabulary(text):
    result = {}
    for element in text.split():
        if element not in result:
            translate = input(f"translate {element}: ")
            chars = '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            for i in chars:
                translate = translate.replace(i, '')
            while translate.isspace() or translate == "":
                translate = input(f"translate {element}: ")
            result[element] = translate.lower()
    return result


def translate(text, dictionary):
    for element in text.split():
        result = []
        if element in dictionary.keys():
            result.append(dictionary.values())
    return result


if __name__ == "__main__":
    TEXT = "Shakespeare's sonnets are poems" \
        " that William Shakespeare wrote on a variety of themes." \
    \
              " When discussing or referring to Shakespeare’s sonnets, it is almost always a reference to the 154 sonnets"
    vocabulary = get_vocabulary(TEXT)
    some_var = (sorted(vocabulary.values()))
    some_var = str(some_var)
    translate(TEXT, vocabulary)
    chars = '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for i in chars:
        some_var = some_var.replace(i, '')
    print(str(some_var))
