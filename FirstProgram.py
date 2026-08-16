fruits = ["apple", "mango", "banana", "guava", "strawberry", "pineapple"]


def printList(list, index=0):
    if index == len(list):
        return

    print(list[index], end=" ")
    printList(list, index + 1)


printList(fruits, 0)
