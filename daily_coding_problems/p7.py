# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as
# 'aaa', 'ka', and 'ak'.

def valid_char_int(s):
    if not s or len(s) > 2 or s[0] == '0':
        return 0
    i = int(s)
    return i >= 1 and i <= 26

def count_decodings(s):
    if len(s) <= 2:
        return valid_char_int(s) \
                + (valid_char_int(s[:1]) and valid_char_int(s[1:]))

    count = 0
    if valid_char_int(s[:1]):
        count += count_decodings(s[1:])
    if valid_char_int(s[:2]):
        count += count_decodings(s[2:])
    return count


print(count_decodings(""))
print(count_decodings("10"))
print(count_decodings("127"))
print(count_decodings("101"))
print(count_decodings("121"))
print(count_decodings("111"))
