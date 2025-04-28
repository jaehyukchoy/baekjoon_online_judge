import sys
input = sys.stdin.readline

def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

T = int(input())
for _ in range(T):
    s = input().strip()
    l, r = 0, len(s) - 1
    ans = 0

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1):
                ans = 1
            else:
                ans = 2
            break
    print(ans)
