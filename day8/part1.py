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
        lines = f.read().splitlines()
        f.close()

        rows, cols = len(lines), len(lines[0])

        nodes = defaultdict(list)

        for i in range(rows):
            for j in range(cols):
                if lines[i][j] != '.':
                    nodes[lines[i][j]].append((i, j))

        antinodes = defaultdict(list)

        for freq, values in nodes.items():
            if len(values) > 1:
                for a in range(len(values)):
                    for b in range(len(values))[a+1:]:
                        diff_i = values[b][0]-values[a][0]
                        diff_j = values[b][1]-values[a][1]

                        if 0 <= values[a][0]-diff_i < rows and 0 <= values[a][1]-diff_j < cols:
                            antinodes[freq].append((values[a][0]-diff_i, values[a][1]-diff_j))

                        if 0 <= values[b][0]+diff_i < rows and 0 <= values[b][1]+diff_j < cols:
                            antinodes[freq].append((values[b][0]+diff_i, values[b][1]+diff_j))

        antinodes_all = set(coord for v in antinodes.values() for coord in v)

        return len(antinodes_all)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()