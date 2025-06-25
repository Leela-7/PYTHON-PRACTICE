def max(*values, **keyvalue):
    if len(values) > 0:
        m = values[0]
        for value in values:
            if value > m:
                m = value
        return m
    elif len(keyvalue) > 0:
        A = list(keyvalue.items())
        max_value = A[0]
        for t in A:
            if t[1] > max_value[1]:
                max_value = t
        return max_value
    else:
        return None

total=max(1, 2, 3, 4, 5)
print("The maximum is", total)
total=max(one=1, two=2, three=3, four=4, five=5)
print("The maximum is", total)
total=max()
print("The maximum is", total)