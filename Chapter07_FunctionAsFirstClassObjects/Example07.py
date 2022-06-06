fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]


if __name__ == '__main__':
    sorted(fruits, key=lambda word: word[::-1])
