
def the_same(basket, fruit):

    if basket[0] == fruit:
        return True

    elif basket[1] == fruit:
        return True

    return False

def totalFruit(fruits):
    if len(fruits) == 0:
        return 0

    start      = 0
    max_fruits = 0
    basket     = [-1] * 2
    basket[0]  = fruits[0]
    index      = 1
    while index < len(fruits):
        if fruits[index] != fruits[index-1]:
            break
        index +=1
    # assign fruit to second basket
    if len(fruits) == index:
        return len(fruits)
    
    basket[1] = fruits[index]

    # return early if we have reached the end of the array

    if len(fruits)-1 == index:
        return index - start + 1

    for index in range(len(fruits)): 

        fruit = fruits[index]

        if not the_same(basket, fruit):

            basket[0] = fruit
            basket[1] = fruits[index-1]
            max_fruits = max(max_fruits, index-start)
            start = index-1
            while fruits[start] == fruits[start-1]:
                start-=1
        else:
            max_fruits = max(max_fruits, index-start+1)
        index +=1
    return max_fruits
if __name__ == "__main__":

    fruits = [0,1,6,6,4,4,6] 
    res = totalFruit(fruits)
    print(res)

