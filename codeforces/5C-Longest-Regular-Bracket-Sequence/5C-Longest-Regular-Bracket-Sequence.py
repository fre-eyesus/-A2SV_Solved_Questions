s = input()

stack = [-1]
longest = 0
count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()

        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]

            if length > longest:
                longest = length
                count = 1
            elif length == longest:
                count += 1

if longest == 0:
    print(0,1)
else:
    print(longest,count)