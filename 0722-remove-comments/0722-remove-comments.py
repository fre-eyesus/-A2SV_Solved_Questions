

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        newline = ""

        for line in source:
            i = 0
            if not in_block:
                newline = ""
            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 1
                    else:
                        newline += line[i]
                else:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 1
                i += 1

            if not in_block and newline:
                res.append(newline)

        return res
