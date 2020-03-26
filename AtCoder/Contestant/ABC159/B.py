def palindrome(string): return 1 if string == string[::-1] else 0


s = input()
N = len(s)
# print(s[0:(N - 1) // 2])
# print(s[(N + 3) // 2 - 1:N])

if palindrome(s[0:(N - 1) // 2]) and palindrome(s[(N + 3) // 2 - 1:N]) and palindrome(s):
    print("Yes")
else:
    print("No")
