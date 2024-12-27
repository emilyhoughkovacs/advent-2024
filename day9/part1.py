import sys
import os
import math
from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'input.txt'
        f = open(file, 'r')
        line = f.read()
        f.close()

        sol = list()

        for i, val in zip(range(len(line)), line):
            if i%2==0:
                for j in range(int(val)):
                    sol.append( int(i/2) )
            else:
                for j in range(int(val)):
                    sol.append( -1 )

        a = 0
        b = len(sol)-1

        while a < b:
            if sol[a] == -1:
                if sol[b] != -1:
                    temp = sol[a]
                    sol[a] = sol[b]
                    sol[b] = temp
                else:
                    b -= 1
            else:
                a += 1

        checksum = 0

        for index, num in enumerate(sol):
            if num != -1:
                checksum += index * num

        return checksum

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()