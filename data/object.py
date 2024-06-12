a = { 1, 2, 3, 4 }
b = { 4, 5, 6, 7 }
c = { 3, 4, 6, 7 }

obj = {
    'a': a,
    'b': b,
    'c': c
}
# Result: dict_keys(['a', 'b', 'c'])
print(obj.keys())

# Result: dict_values([{1, 2, 3, 4}, {4, 5, 6, 7}, {3, 4, 6, 7}])
print(obj.values())

# Result: dict_items([('a', {1, 2, 3, 4}), ('b', {4, 5, 6, 7}), ('c', {3, 4, 6, 7})])
print(obj.items())

# Result: {1, 2, 3, 4}
print(obj.get('a'))

# Result: {4, 5, 6, 7}
print(obj.pop('b'))

# Result: ('c', {3, 4, 6, 7})
print(obj.popitem())

# Result: 1
print(len(obj))

# Result: True
print('a' in obj)

# Result: False
print('b' not in obj)

# Result: dict_keys(['a', 'b', 'c'])
print(obj.keys())

# Result: dict_values([{1, 2, 3, 4}, {4, 5, 6, 7}, {3, 4, 6, 7}])
print(obj.values())

# Result: dict_items([('a', {1, 2, 3, 4}), ('b', {4, 5, 6, 7}), ('c', {3, 4, 6, 7})])
print(obj.items())

# Result: {1, 2, 3, 4}
print(obj.get('a'))

# Result: {4, 5, 6, 7}
print(obj.pop('b'))

# Result: ('c', {3, 4, 6, 7})
print(obj.popitem())

# Result: 1
print(len(obj))

# Result: True
print('a' in obj)

# Result: False
print('b' not in obj)
