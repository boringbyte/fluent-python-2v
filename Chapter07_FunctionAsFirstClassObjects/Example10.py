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


def tags_positional(name, /, *content, class_=None, **attrs):
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
    print(tag('br'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', class_='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
    print(tag(**my_tag))
    print('-------------Positional Tags Starting-------------')
    print(tags_positional('br'))
    print(tags_positional('p', 'hello', 'world'))
    print(tags_positional('p', 'hello', id=33))
    print(tags_positional('p', 'hello', 'world', class_='sidebar'))
    print(tags_positional(content='testing', name='img'))
    print(tags_positional(**my_tag))
