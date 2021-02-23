def isPangram(s):
    str = list(s)
    az = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    result = all(x.lower() in str or x.upper() in str for x in az)
    print(result)


def oddOrEvenOneOut(n):
    odd = []
    even = []

    numbers = n.split()
    for x in numbers:
        if int(x) % 2 == 0:
            even.append(numbers.index(x))
        else:
            odd.append(numbers.index(x))

    oddLen = len(odd)

    if oddLen == 1:
        print("Odd one is at position {}".format((odd[0] + 1)))
        return odd[0] + 1
    else:
        print("Even one is at position {}".format((even[0] + 1)))
        return even[0] + 1


def breakIntoPairs(str):
    stringToOperate = str if len(str) % 2 == 0 else str + "_"
    arr = []
    for x in range(0, len(stringToOperate), 2):
        arr.append(stringToOperate[x : x + 2])
    print(arr)
