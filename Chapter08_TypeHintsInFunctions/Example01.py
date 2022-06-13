def show_count(count, word):
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'


if __name__ == '__main__':
    print(show_count(99, 'bird'))
    print(show_count(1, 'bird'))
    print(show_count(0, 'bird'))
