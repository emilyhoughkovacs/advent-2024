import sys
import os
import math

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'input.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [[y for y in x] for x in lines]

        direction = 'up'

        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == '^':
                    break
            else:
                continue
            break

        print(i, j)

        offgrid = False

        def moveup(lines, i, j, direction, offgrid=False):
            lines[i][j] = 'X'
            while i-1 >= 0 and lines[i-1][j] != '#':
                i = i-1
                lines[i][j] = 'X'
            if i-1 < 0:
                offgrid = True
            direction = 'right'

            return lines, i, j, direction, offgrid

        def moveright(lines, i, j, direction, offgrid=False):
            lines[i][j] = 'X'
            while j+1 < len(lines[0]) and lines[i][j+1] != '#':
                j = j+1
                lines[i][j] = 'X'
            if j+1 >= len(lines[0]):
                offgrid = True
            direction = 'down'

            return lines, i, j, direction, offgrid

        def movedown(lines, i, j, direction, offgrid=False):
            lines[i][j] = 'X'
            while i+1 < len(lines) and lines[i+1][j] != '#':
                i = i+1
                lines[i][j] = 'X'
            if i+1 >= len(lines):
                offgrid = True
            direction = 'left'

            return lines, i, j, direction, offgrid


        def moveleft(lines, i, j, direction, offgrid=False):
            lines[i][j] = 'X'
            while j-1 >= 0 and lines[i][j-1] != '#':
                j = j-1
                lines[i][j] = 'X'
            if j-1 < 0:
                offgrid = True
            direction = 'up'

            return lines, i, j, direction, offgrid

        while offgrid == False:
            if direction == 'up':
                lines, i, j, direction, offgrid = moveup(lines, i, j, direction, offgrid)
                for line in lines:
                    print(line)
                print()
            elif direction == 'right':
                lines, i, j, direction, offgrid = moveright(lines, i, j, direction, offgrid)

                for line in lines:
                    print(line)
                print()
            elif direction == 'down':
                lines, i, j, direction, offgrid = movedown(lines, i, j, direction, offgrid)

                for line in lines:
                    print(line)
                print()
            elif direction == 'left':
                lines, i, j, direction, offgrid = moveleft(lines, i, j, direction, offgrid)

                for line in lines:
                    print(line)
                print()

        for line in lines:
            print(line)

        count = 0

        for a in range(len(lines)):
            for b in range(len(lines[0])):
                if lines[a][b] == 'X':
                    count += 1

        return count

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()