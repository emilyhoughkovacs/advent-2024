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
        lines = f.read()
        f.close()

        rules = lines.split('\n\n')[0]
        updates = lines.split('\n\n')[1]

        rules = rules.split('\n')

        rules = [x.split('|') for x in rules]
        rules = [[int(x) for x in rule] for rule in rules]

        updates = updates.split('\n')
        updates = [update.split(',') for update in updates]
        updates = [[int(x) for x in instruction] for instruction in updates]

        isInvalid = list()

        def invalid(sequence):
            myMap = dict(zip(sequence, range(len(sequence))))
            for pair in rules:
                if pair[0] in myMap and pair[1] in myMap:
                    if myMap[pair[0]] > myMap[pair[1]]:
                        return True


        for row in updates:
            if invalid(row):
                isInvalid.append(row)

        # isValid = [row for row in updates if row not in isInvalid]

        # theSum = 0

        # for valid in isValid:
        #     theSum += valid[math.floor(len(valid)/2)]

        # return theSum

        # print(isInvalid)

        for myRow in isInvalid:
            tempMap = dict(zip(myRow, range(len(myRow))))
            while invalid(myRow):
                for r in rules:
                    if r[0] in tempMap and r[1] in tempMap:
                        if tempMap[r[0]] > tempMap[r[1]]:
                            myRow[tempMap[r[0]]], myRow[tempMap[r[1]]] = myRow[tempMap[r[1]]], myRow[tempMap[r[0]]] 
                            tempMap[r[0]], tempMap[r[1]] = tempMap[r[1]], tempMap[r[0]]

        # print(isInvalid)

        theSum = 0

        for newly_valid in isInvalid:
            theSum += newly_valid[math.floor(len(newly_valid)/2)]

        return theSum

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()