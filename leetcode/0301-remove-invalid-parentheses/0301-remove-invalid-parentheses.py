class Solution(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        if index == len(string):

            if left_count == right_count:

                if rem_count <= self.min_removed:
                    possible_ans = "".join(expr)

                    # If the current count of brackets removed < current minimum, ignore
                    # previous answers and update the current minimum count.
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)    
        else:        

            current_char = string[index]

            # If the current character is not a parenthesis, just recurse one step ahead.
            if current_char != '(' and  current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                # Else, one recursion is with ignoring the current character.
                # So, we increment the ignored counter and leave the left and right untouched.
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)

                expr.append(current_char)

                # If the current parenthesis is an opening bracket, we consider it
                # and increment left and  move forward
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
                elif right_count < left_count:
                    # If the current parenthesis is a closing bracket, we consider it only if we
                    # have more number of opening brackets and increment right and move forward.
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)

                expr.pop()

    def removeInvalidParentheses(self, s):

        self.reset()

        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)