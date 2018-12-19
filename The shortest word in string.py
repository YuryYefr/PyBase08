from string import digits


def opredelim(text, some_filt):  #removing all digits
    result = ""
    for i in text:
        if i not in some_filt:
            result += i

    return result


if __name__ == "__main__":
    text = input("some text")
    some_filt = digits
    text_res = opredelim(text, some_filt).split()
    res = min(text_res, key=len)  #find the shortest element in text,
    print(res)

