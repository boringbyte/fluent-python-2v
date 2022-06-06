def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


if __name__ == '__main__':
    from functools import partial
    print(tag)
    picture = partial(tag, 'img', class_='pic-frame')
    print(picture(src='wumpus.jpg'))
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
