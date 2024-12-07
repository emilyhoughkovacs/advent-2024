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

        nums = [l.split(' ') for l in lines]
        nums = [[int(num) for num in line] for line in nums]

        safe = 0

        def isSafe(row):
            if sorted(row)!=row and sorted(row, reverse=True)!=row:
                return False
            for i in range(len(row)-1):
                if abs(row[i] - row[i+1]) > 3 or abs(row[i] - row[i+1]) < 1:
                    return False
            # print(row)
            return True

        def isSafeNow(row):
            for j in range(len(row)):
                if j == 0:
                    if isSafe(row[1:]):
                        return True
                    continue
                elif j == len(row)-1:
                    if isSafe(row[:-1]):
                        return True
                    continue
                else:
                    if isSafe(row[:j] + row[j+1:]):
                        return True
                    continue
                return False
                # print(j, ",", row[j])

        for line in nums:
            if isSafe(line):
                safe += 1
            elif isSafeNow(line):
                safe += 1
            # print("====")

        return safe

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()