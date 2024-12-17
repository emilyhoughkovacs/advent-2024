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

        # forwards and backwards

        for row in lines:
            theCount += row.count('XMAS')
            theCount += row.count('SAMX')

        # up and down

        transposed = [[char for char in row] for row in lines]

        for i in range(len(lines)):
            for j in range(i, len(lines[0])):
                transposed[i][j], transposed[j][i] = lines[j][i], lines[i][j]

        transposed = [''.join(x) for x in transposed]
        
        for row in transposed:
            theCount += row.count('XMAS')
            theCount += row.count('SAMX')

        # diagonals

        downright = 0
        downleft = 0
        upright = 0
        upleft = 0

        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == 'X':
                    try:
                        if lines[i+1][j+1] == 'M' and i+1 <= len(lines) and j+1 <= len(lines[0]):
                            try:
                                if lines[i+2][j+2] == 'A' and i+2 <= len(lines) and j+2 <= len(lines[0]):
                                    try:
                                        if lines[i+3][j+3] == 'S' and i+3 <= len(lines) and j+3 <= len(lines[0]):
                                            theCount += 1 
                                            downright += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
                    try:
                        if lines[i+1][j-1] == 'M' and j-1 >= 0 and i+1 <= len(lines):
                            try:
                                if lines[i+2][j-2] == 'A' and j-2 >= 0 and i+2 <= len(lines):
                                    try:
                                        if lines[i+3][j-3] == 'S' and j-3 >= 0 and i+3 <= len(lines):
                                            theCount += 1 
                                            downleft += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
                    try:
                        if lines[i-1][j+1] == 'M' and i-1 >= 0 and j+1 <= len(lines[0]):
                            try:
                                if lines[i-2][j+2] == 'A' and i-2 >= 0 and j+2 <= len(lines[0]):
                                    try:
                                        if lines[i-3][j+3] == 'S' and i-3 >= 0 and j+3 <= len(lines[0]):
                                            theCount += 1 
                                            upright += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
                    try:
                        if lines[i-1][j-1] == 'M' and j-1 >= 0 and i-1 >= 0:
                            try:
                                if lines[i-2][j-2] == 'A' and j-2 >= 0 and i-2 >= 0:
                                    try:
                                        if lines[i-3][j-3] == 'S' and j-3 >= 0 and i-3 >= 0:
                                            theCount += 1 
                                            upleft += 1
                                            # print(i, j)
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass


        # print('downright', downright)
        # print('downleft', downleft)
        # print('upright', upright)
        # print('upleft', upleft)
        return theCount

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()