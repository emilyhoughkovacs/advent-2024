import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'input.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        theCount = 0

        # diagonals

        for i in range(len(lines))[1:-1]:
            for j in range(len(lines[0]))[1:-1]:
                if lines[i][j] == 'A':
                    if (lines[i+1][j+1] == 'M' and lines[i-1][j-1] == 'S') or (lines[i+1][j+1] == 'S' and lines[i-1][j-1] == 'M'):
                        if (lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S') or (lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M'):
                            theCount += 1
                    # try:
                    #     if lines[i+1][j+1] == 'M' and i+1 <= len(lines) and j+1 <= len(lines[0]):
                    #         try:
                    #             if lines[i+2][j+2] == 'A' and i+2 <= len(lines) and j+2 <= len(lines[0]):
                    #                 try:
                    #                     if lines[i+3][j+3] == 'S' and i+3 <= len(lines) and j+3 <= len(lines[0]):
                    #                         theCount += 1 
                    #                         downright += 1
                    #                 except:
                    #                     pass
                    #         except:
                    #             pass
                    # except:
                    #     pass
                    # try:
                    #     if lines[i+1][j-1] == 'M' and j-1 >= 0 and i+1 <= len(lines):
                    #         try:
                    #             if lines[i+2][j-2] == 'A' and j-2 >= 0 and i+2 <= len(lines):
                    #                 try:
                    #                     if lines[i+3][j-3] == 'S' and j-3 >= 0 and i+3 <= len(lines):
                    #                         theCount += 1 
                    #                         downleft += 1
                    #                 except:
                    #                     pass
                    #         except:
                    #             pass
                    # except:
                    #     pass
                    # try:
                    #     if lines[i-1][j+1] == 'M' and i-1 >= 0 and j+1 <= len(lines[0]):
                    #         try:
                    #             if lines[i-2][j+2] == 'A' and i-2 >= 0 and j+2 <= len(lines[0]):
                    #                 try:
                    #                     if lines[i-3][j+3] == 'S' and i-3 >= 0 and j+3 <= len(lines[0]):
                    #                         theCount += 1 
                    #                         upright += 1
                    #                 except:
                    #                     pass
                    #         except:
                    #             pass
                    # except:
                    #     pass
                    # try:
                    #     if lines[i-1][j-1] == 'M' and j-1 >= 0 and i-1 >= 0:
                    #         try:
                    #             if lines[i-2][j-2] == 'A' and j-2 >= 0 and i-2 >= 0:
                    #                 try:
                    #                     if lines[i-3][j-3] == 'S' and j-3 >= 0 and i-3 >= 0:
                    #                         theCount += 1 
                    #                         upleft += 1
                    #                         # print(i, j)
                    #                 except:
                    #                     pass
                    #         except:
                    #             pass
                    # except:
                    #     pass

        return theCount

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()