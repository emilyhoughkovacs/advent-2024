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

        integers = [str(i) for i in range(10)]

        lines = [[l for l in line if l in integers] for line in lines]

        theSum = 0

        for line in lines:
            first = line[0]
            last = line[-1]
            num = int(first+last)
            theSum += num

        return theSum

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()