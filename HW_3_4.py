from string import whitespace, punctuation


def get_vocabulary(text):
    result = {}
    for element in text.split():
        if element not in result:
            translate = input(f"translate {element}: ").lower()
            chars = '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            for i in chars:
                translate = translate.replace(i, '')
            while translate.isspace():
                translate = input(f"translate {element}: ")
            result[element] = translate
    return result


def krasivii_dict(dict):
    print(f"{'Word':<30} {'Translate':<30}")
    for k, v in dict.items():
        print(f'{k:<30} {v:<30}')


if __name__ == "__main__":
    TEXT = "Shakespeare's " \
           "sonnets are poems that William Shakespeare wrote on a variety of themes." \
 \
           " When discussing or referring to Shakespeare’s sonnets, it is almost always a reference to the 154 sonnets"
    vocabulary = get_vocabulary(TEXT.lower())
    krasivii_dict(vocabulary)
