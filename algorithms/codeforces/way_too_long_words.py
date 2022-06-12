import sys
input = sys.stdin.readlines


def main():
    lines = [line.strip() for line in input()]
    limit = 10 
    new_words = []
    for word in lines[1:]:
        if len(word) > limit:
            new_words.append(word[0] + str(len(word[1:len(word)-1])) + word[-1])
        else:
            new_words.append(word)
    print('\n'.join(new_words))
if __name__ == "__main__":
    main()
