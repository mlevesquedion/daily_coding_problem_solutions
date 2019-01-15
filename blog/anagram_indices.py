def anagram_indices(word, s):
    s_word = sorted(word)
    indices = []
    for i in range(len(s) - len(word) + 1):
        if sorted(s[i:i+len(word)]) == s_word:
            indices.append(i)
    return indices


if __name__ == '__main__':
    print(anagram_indices('ab', 'abxaba'))
