from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
hyphenate = methodcaller('replace', ' ', '-')

if __name__ == '__main__':
    print(upcase(s))
    print(hyphenate(s))
