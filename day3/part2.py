import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'input.txt'
        f = open(file, 'r')
        line = f.read()
        f.close()

        # parse by don't
        parsed = line.split("don't()")

        # for x in parsed:
        #     print(x)

        # process before the first don't

        beginning = parsed[0]
        beginning_parsed = [l[:8] for l in beginning.split('mul(') if ')' in l[:8]]

        theSum = 0

        for candidate in beginning_parsed:
            if ',' not in candidate:
                continue
            candidate = candidate.split(')')[0]
            candidate = candidate.split(',')

            try:
                num1 = int(candidate[0])
                num2 = int(candidate[1])
            except:
                continue

            if num1 > 0 and num1 < 1000 and num2 > 0 and num2 < 1000:
                theSum += num1 * num2

        parsed = [x.split('do()')[1:] for x in parsed[1:]]

        parsed = [''.join(x) for x in parsed]

        for section in parsed:
            section_parsed = [l[:8] for l in section.split('mul(') if ')' in l[:8]]

            for candidate in section_parsed:
                if ',' not in candidate:
                    continue
                candidate = candidate.split(')')[0]
                candidate = candidate.split(',')

                try:
                    num1 = int(candidate[0])
                    num2 = int(candidate[1])
                except:
                    continue

                if num1 > 0 and num1 < 1000 and num2 > 0 and num2 < 1000:
                    theSum += num1 * num2


        return theSum

        # parsed = [l[:8] for l in line.split('mul(') if ')' in l[:8]]
        # # print(parsed)

        # for candidate in parsed:
        #     if ',' not in candidate:
        #         continue
        #     candidate = candidate.split(')')[0]
        #     candidate = candidate.split(',')

        #     try:
        #         num1 = int(candidate[0])
        #         num2 = int(candidate[1])
        #     except:
        #         continue

        #     if num1 > 0 and num1 < 1000 and num2 > 0 and num2 < 1000:
        #         theSum += num1 * num2



        # parsed = [l.split(')')[0] for l in parsed if ',' in l]
        # parsed = [l.split(',') for l in parsed]
        # print(parsed)
        # for pairs in parsed:
        #     print(pairs)
        # nums = [[int(num) for num in line] for line in parsed]

        # theSum = 0
        # for a, b in nums:
        #     if a > 0 and a < 1000 and b > 0 and b < 1000:
        #         theSum += a * b

        # return theSum

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()