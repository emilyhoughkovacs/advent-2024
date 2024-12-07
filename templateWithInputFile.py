def solution():
    f = open('inputfile.txt', 'r')
    lines = f.read().splitlines()
    f.close()

    return lines

def main():
    print(solution())

if __name__ == '__main__':
    main()