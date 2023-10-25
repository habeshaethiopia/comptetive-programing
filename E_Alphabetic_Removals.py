n, k = map(int, input().split())
s = list(input().strip())
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1
for i in range(26):
    if freq[i] > 0:
        ch = chr(i + ord('a'))
        cnt = min(k, freq[i])
        k -= cnt
        for j in range(len(s)):
            if s[j] == ch:
                s[j] = ''
                cnt -= 1
                if cnt == 0:
                    break
    if k == 0:
        break
print(''.join(s))