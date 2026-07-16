tarer = ['a','e','e','a','d','d','a','a','a','a','a','a','a']
tesakner = set(tarer)
b = {}
for i in tesakner:
    m = 0
    for j in tarer:
        if j == i:
            m += 1
    b[i] = m
print(b)
#text
