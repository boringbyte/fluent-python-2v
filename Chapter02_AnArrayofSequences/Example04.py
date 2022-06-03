colors = ['black', 'white']
sizes = ['S', 'M', 'L']


if __name__ == '__main__':
    tshirts = [(color, size) for color in colors for size in sizes]
    for tshirt in tshirts:
        print(tshirt)
    print('-----------------')
    tshirts = [(color, size) for size in sizes for color in colors]
    for tshirt in tshirts:
        print(tshirt)
