


def generate_hashtag(string):
    string = ''.join([word.capitalize() for word in string.split(' ')])
    if len(string) + 1 >= 140 or len(string) == 0:
        return false
    return '#' + string

if __name__ == "__main__":
    s = 'c i n'
    s = generate_hashtag(s)
    print(s)
