def reverse_vowels(in_str):
    in_str = list(in_str)
    vowels = "aeiou"
    blocked = []
    for idx, letter in enumerate(in_str):
        if idx in blocked:
            break
        if letter in vowels:
            blocked.append(idx)
            for idx_2, letter_2 in enumerate(in_str[::-1]):
                if letter_2 in vowels:
                    idx_3 = len(in_str) - idx_2 - 1
                    if idx_3 in blocked:
                        continue
                    blocked.append(idx_3)
                    in_str[idx_3], in_str[idx] = in_str[idx], in_str[idx_3]
                    break
    return in_str


res = reverse_vowels('hello werlad')
print(res)
