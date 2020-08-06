def reverse_vowels(in_str):
    in_str = list(in_str)
    vowels = "aeiou"
    letters = []
    for idx in range(len(in_str)):
        if in_str[idx].lower() in vowels:
            letters.append(in_str[idx])
            in_str[idx] = None

    for idx in range(len(in_str)):
        if not in_str[idx]:
            in_str[idx] = letters.pop(-1)
    in_str = ''.join(in_str)
    return in_str


res = reverse_vowels('hAllo werlad')
print(res)
