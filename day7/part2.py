import sys
import os
import math
from itertools import product

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'input.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [line.split(': ') for line in lines]
        lines = [[l[0]] + l[1].split(' ') for l in lines]
        lines = [[int(n) for n in row] for row in lines]

        total = 0

        def evaluate_equation(numbers, operators):
            """Evaluate the equation left-to-right using the given operators."""
            result = numbers[0]
            for i in range(len(operators)):
                if operators[i] == '+':
                    result += numbers[i + 1]
                elif operators[i] == '*':
                    result *= numbers[i + 1]
                elif operators[i] == '|':
                    result = str(result)
                    toconcat = str(numbers[i + 1])
                    result = int(result + toconcat)
            return result

        total_sum = 0
        
        for equation in lines:
            target, numbers = equation[0], equation[1:]
            n = len(numbers)
            operator_combinations = product('+*|', repeat=n-1)
            
            # Check each operator combination
            for ops in operator_combinations:
                if evaluate_equation(numbers, ops) == target:
                    total_sum += target
                    break  # No need to check more combinations for this equation
        
        return total_sum


        # def is_valid(equation):
        #     result = equation[0]
        #     eq = equation[1:]
        #     operators = ['+', '*']

        #     start = eq[0]

        #     # for i, e in enumerate(eq[1:]):
        #     #     for op in operators:
        #     #         if op == '+':
        #     #             start = start + e
        #     #         if op == '*':
        #     #             start = start * e
        #     #         print(op, e, start)

        #     for i in range(len(eq[1:]) + 1)[1:]:
        #         for e in eq[1:]:
        #             for op in operators:
        #                 print(op, e)

        #     print()
        #     return True

        # for r in lines:
        #     if is_valid(r):
        #         total += 1

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()