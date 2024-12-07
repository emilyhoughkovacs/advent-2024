import ast
import sys

class Solution(object):
    def __init__(self):
        # for input with arrays
        args = [ast.literal_eval(arg) for arg in sys.argv[1:]]
        # self.args = [arg for arg in sys.argv[1:]]
        self.arg1 = args[0]

    def solution(self, arg1):

        # prints first command line argument
        return arg1

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()