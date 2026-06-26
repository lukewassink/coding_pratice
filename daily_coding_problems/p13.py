# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with
# k distinct characters is "bcb".

def longest(s, k):
    seen = {}
    total_seen = 0
    start = 0
    end = 0
    max_len = 0

    while end < len(s):
        if total_seen <= k:
            cur = s[end]
            seen[cur] = 1 + seen.get(cur, 0)
            if seen[cur] == 1: total_seen += 1
            end += 1
        else:
            cur = s[start]
            seen[cur] -= 1
            if seen[cur] == 0:
                del seen[cur]
                total_seen -= 1
            start += 1

        if total_seen <= k: max_len = max(max_len, end - start)

    return max_len

print(longest("", 2)) # 0
print(longest("abcba", 0)) # 0
print(longest("abcba", 2)) # 3
print(longest("abbcba", 1)) # 2
print(longest("abbcebacbac", 3)) # 6
