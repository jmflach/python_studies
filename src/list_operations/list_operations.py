
def my_insert(list, index, element):
    return list[:index] + [element] + list[index:]

def my_pop(list, index):
    return list[:index] + list[index+1:]

def my_index(list, element):
    index = 0
    for i in list:
        if i == element:
            return index
        index += 1

def my_remove(list, element):
    i = my_index(list, element)
    return my_pop(list, i)

def my_reverse(list):
    return list[::-1]

def main():
    print('Testing list operations')

    l = [0,1,2,3,4,5,6,7,8,9,'banana', 'apple', 'oranges']

    print(l)

    l.pop()

    print(l)

    l.append('strawberry')

    print(l)

    l.append([1,2,3])

    print(l)

    l += [1,2,3]

    print(l)

    l.insert(0, '0th')

    print(l)

    l = my_insert(l, 1, '1st')

    print(l)

    l.pop(1)

    print(l)

    l = my_pop(l, 1)

    print(l)

    print(l.index('banana'))
    print(my_index(l, 'banana'))

    l = my_remove(l, 'banana')

    print(l)

    l = my_reverse(l)

    print(l)


if __name__ == '__main__':
    main()