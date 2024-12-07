# import ast
import sys

class Solution(object):
    def __init__(self):
        # for input with arrays
        # self.args = [ast.literal_eval(arg) for arg in sys.argv[1:]]
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # prints first command line argument
        return args[0]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()