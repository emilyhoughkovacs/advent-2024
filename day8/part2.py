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

        for freq, positions in nodes.items():
            n = len(positions)
            if n > 1:
                for a in range(n):
                    for b in range(n)[a+1:]:
                        pos_i1, pos_j1 = positions[a][0], positions[a][1]
                        pos_i2, pos_j2 = positions[b][0], positions[b][1]

                        diff = 1

                        diff_i = pos_i2 - pos_i1
                        diff_j = pos_j2 - pos_j1

                        # backward antinode
                        i_back, j_back = pos_i1 - diff_i, pos_j1 - diff_j
                        while(0 <= i_back < rows and 0 <= j_back < cols):
                            print('back')
                            print(pos_i1, pos_j1, pos_i2, pos_j2)
                            print(i_back, j_back)
                            print()
                            antinodes[freq].append((i_back, j_back))
                            diff += 1
                            i_back, j_back = pos_i1 - diff_i*diff, pos_j1 - diff_j*diff

                        diff_i = pos_i2 - pos_i1
                        diff_j = pos_j2 - pos_j1

                        # # backward antinode 2
                        # i_back, j_back = pos_i1 - diff_i, pos_j1 - diff 
                        # while(0 <= i_back < rows and 0 <= j_back < cols):
                        #     print(pos_i1, pos_j1, pos_i2, pos_j2)
                        #     print(i_back, j_back)
                        #     print()
                        #     antinodes[freq].append((i_back, j_back))
                        #     diff += 1
                        #     i_back, j_back = pos_i1 - diff_i*diff, pos_j1 - diff

                        diff = 1

                        diff_i = pos_i2 - pos_i1
                        diff_j = pos_j2 - pos_j1

                        # forward antinode
                        i_forward, j_forward = pos_i2 + diff_i, pos_j2 + diff_j
                        while(0 <= i_forward < rows and 0 <= j_forward < cols):
                            print('forward')
                            print(pos_i1, pos_j1, pos_i2, pos_j2)
                            print(i_forward, j_forward)
                            print()
                            antinodes[freq].append((i_forward, j_forward))
                            diff += 1
                            i_forward, j_forward = pos_i2 + diff_i*diff, pos_j2 + diff_j*diff

                        # diff = 1

                        # i_forward, j_forward = pos_i2 + diff_i, pos_j2 + diff
                        # while(0 <= i_forward < rows and 0 <= j_forward < cols):

                        #     print(pos_i1, pos_j1, pos_i2, pos_j2)
                        #     print(i_forward, j_forward)
                        #     print()
                        #     antinodes[freq].append((i_forward, j_forward))
                        #     diff += 1
                        #     i_forward, j_forward = pos_i2 + diff_i*diff, pos_j2 + diff


        antinodes_all = [coord for v in antinodes.values() for coord in v] + [c for val in nodes.values() for c in val if len(val) > 1]
        antinodes_all = set(antinodes_all)

        print(antinodes_all)

        return len(antinodes_all)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()