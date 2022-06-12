import sys
input = sys.stdin.readlines

def main():
    team_views = [line.strip() for line in input()][1:]
    count = 0
    for line in team_views:
        if sum([int(v) for v in line.split(' ')]) >= 2:
            count +=1
    return count




if __name__ == "__main__":
    print(main())


