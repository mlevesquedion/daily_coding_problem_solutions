def solve(s, k):
    substring_start = 0
    current_index = 0
    current_substring = ''
    chars = set()
    longest_substring = ''
    while substring_start < len(s):
        current_char = s[current_index]
        chars.add(current_char)
        if len(chars) > k or current_index > len(s) - 2:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            substring_start += 1
            current_index = substring_start
            current_substring = ''
            chars.clear()
        else:
            current_substring += current_char
            current_index += 1
    return longest_substring


def longest_substring(s, k):
    left = 0
    right = 0
    chars = set()
    longest = ''
    while right < len(s):
        current_char = s[right]
        chars.add(current_char)
        if len(chars) > k:
            string = s[left:right+1]
            if len(string) > len(longest):
                longest = string
            while len(chars) > k:
                chars.remove(s[left])
                left += 1
                chars.add(s[left])
        right += 1
    return longest


if __name__ == '__main__':
    assert solve('abcba', 2) == 'bcb'
