import sys

with open(sys.argv[1]) as f:
    lines = [ int(i) for i in f ]

def main():
    part1()
    part2()

def part1():
    goal = 2020
    for num in lines:
        for num2 in lines:
            if (num+num2 == goal):
                res = num * num2
    print res

def part2():
    goal = 2020
    for num in lines:
        for num2 in lines:
            for num3 in lines:
                if (num+num2+num3 == goal):
                    res = num * num2 * num3
    print res

if __name__ == "__main__":
    main()
