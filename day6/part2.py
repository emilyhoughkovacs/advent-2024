import sys
import os
import math
from copy import deepcopy

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
        templines = deepcopy(lines)

        direction = 'up'

        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == '^':
                    break
            else:
                continue
            break

        start_i, start_j = i, j

        # print(i, j)

        offgrid = False
        numXs = 0

        def moveup(mylines, i, j, direction, numXs, offgrid=False):
            mylines[i][j] = 'X'
            while i-1 >= 0 and mylines[i-1][j] != '#':
                i = i-1
                if mylines[i][j] == 'X':
                    numXs += 1
                else:
                    numXs = 0
                    mylines[i][j] = 'X'
            if i-1 < 0:
                offgrid = True
            direction = 'right'

            return mylines, i, j, direction, numXs, offgrid

        def moveright(mylines, i, j, direction, numXs, offgrid=False):
            mylines[i][j] = 'X'
            while j+1 < len(lines[0]) and mylines[i][j+1] != '#':
                j = j+1
                if mylines[i][j] == 'X':
                    numXs += 1
                else:
                    numXs = 0
                    mylines[i][j] = 'X'
            if j+1 >= len(lines[0]):
                offgrid = True
            direction = 'down'

            return mylines, i, j, direction, numXs, offgrid

        def movedown(mylines, i, j, direction, numXs, offgrid=False):
            mylines[i][j] = 'X'
            while i+1 < len(lines) and mylines[i+1][j] != '#':
                i = i+1
                if mylines[i][j] == 'X':
                    numXs += 1
                else:
                    numXs = 0
                    mylines[i][j] = 'X'
            if i+1 >= len(lines):
                offgrid = True
            direction = 'left'

            return mylines, i, j, direction, numXs, offgrid


        def moveleft(mylines, i, j, direction, numXs, offgrid=False):
            mylines[i][j] = 'X'
            while j-1 >= 0 and mylines[i][j-1] != '#':
                j = j-1
                if mylines[i][j] == 'X':
                    numXs += 1
                else:
                    numXs = 0
                    mylines[i][j] = 'X'
            if j-1 < 0:
                offgrid = True
            direction = 'up'

            return mylines, i, j, direction, numXs, offgrid

        def take_turns(mylines, i, j, direction, numXs, offgrid):

# this <= 100 logic is not very smart and very slow. the problem is if you do numXs <= 1
# then you could count cases where you DO go offgrid but retrace your steps left-to-right when originally you went right-to-left
# but it works so ¯\_(ツ)_/¯ 
            while offgrid == False and numXs <= 100:
                if direction == 'up':
                    mylines, i, j, direction, numXs, offgrid = moveup(mylines, i, j, direction, numXs, offgrid)

                elif direction == 'right':
                    mylines, i, j, direction, numXs, offgrid = moveright(mylines, i, j, direction, numXs, offgrid)

                elif direction == 'down':
                    mylines, i, j, direction, numXs, offgrid = movedown(mylines, i, j, direction, numXs, offgrid)

                elif direction == 'left':
                    mylines, i, j, direction, numXs, offgrid = moveleft(mylines, i, j, direction, numXs, offgrid)

            return offgrid, numXs, mylines

        # offgrid, Xs = take_turns(templines, i, j, direction, numXs, offgrid)
        # templines = lines

        count = 0

        for a in range(len(lines)):
            for b in range(len(lines[0])):
                numXs = 0
                offgrid = False
                if lines[a][b] == '.':
                    templines[a][b] = '#'

                    offgrid, Xs, afterlines = take_turns(templines, i, j, direction, numXs, offgrid)
                    if offgrid == False:
                        count += 1

                    templines[a][b] = '.'
                    templines = [[r if r!='X' else '.' for r in g] for g in templines]
                    templines[start_i][start_j] = '^'

        return count

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()