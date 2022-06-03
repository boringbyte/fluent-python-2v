colors = ['black', 'white']
sizes = ['S', 'M', 'L']


if __name__ == '__main__':
    for tshirt in (f'{c} {s}' for c in colors for s in sizes):
        print(tshirt)
