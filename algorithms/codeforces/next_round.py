import sys
input = sys.stdin.readlines

def main():
    nk, scores = [line.strip().split(' ') for line in input()]
    n, k = [int(number) for number in nk]

    i = k 
    limit = -1 
    for idx,score in enumerate(scores):
        if int(score) == 0:
            limit = idx 
            break

    if limit != -1 and limit < k:
        return 0 if limit == 0 else limit 
    while i < n:
        if int(scores[i]) == 0 or scores[i-1] != scores[i]:
            break
        i +=1
    return i 

if __name__ == "__main__":
    print(main())
