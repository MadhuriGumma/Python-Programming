def char_frequency(str1):
    chars = {}
    for n in str1:
        keys = chars.keys()
        if n in keys:
            chars[n] += 1
        else:
            chars[n] = 1
    return chars
print(char_frequency('gumma madhuri'))