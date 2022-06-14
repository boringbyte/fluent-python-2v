if __name__ == '__main__':
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print(lewis is charles)
    print(id(charles), id(charles))
    lewis['balance'] = 950
    print(charles)
