import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputfile.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        nums = [l.split('   ') for l in lines]
        nums = [[int(num) for num in line] for line in nums]

        left = sorted([num[0] for num in nums])
        right = sorted([num[1] for num in nums])

        theSum = 0

        for x, y in zip(left, right):
            theSum += abs(x-y)

        return theSum

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()