


def can_construct(target_word, words, cache = {}):
    if target_word in cache:
        return cache[target_word]
    if target_word == '':
        return 1 
    count = 0
    for word in words:
        if target_word.startswith(word):
            res = can_construct(target_word[len(word):], words, cache)
            count += res
            cache[target_word] = count

    return count 


res = can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])
print(res)
