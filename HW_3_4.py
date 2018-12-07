import pprint
from string import whitespace, punctuation


def get_vocabulary(text):
    result = {}
    for element in text.split():
        if element not in result:
            translate = input(f"translate {element}: ")
            while translate.isspace():
                translate = input(f"translate {element}: ")
            result[element] = translate
    return result


if __name__ == "__main__":
    TEXT = "Shakespeare's " \
           "sonnets are poems that William Shakespeare wrote on a variety of themes." \
 \
           " When discussing or referring to Shakespeare’s sonnets, it is almost always a reference to the 154 sonnets"
    vocabluary = get_vocabluary(TEXT)
    pprint.pformat(vocabluary)
