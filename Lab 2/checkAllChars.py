import string
alphabet = set(string.ascii_lowercase)
print(alphabet)
string1 = 'We promptly judged antique ivory buckles for the next prize'
print(set(string1.lower()) >= alphabet)
string2 = 'The quick brown fox jumps over the lazy cat'
print(set(string2.lower()) >= alphabet)