contacts = {
    'naresh': 998878899,
    'suresh': 556676677,
    'ramesh': 556778975,
    'kishore': 776566784
}

names = contacts.keys()
print(names)
for name in names:
    print(name)

values = contacts.values()
print(values)
for value in values:
    print(value)

items = contacts.items()
print(items)
for i in items:
    print(i[0], i[1])
