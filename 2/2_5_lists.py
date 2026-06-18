lts = [3, 5, 7, 9, 10.5]
print(lts)
lts.append('Python')
print(len(lts))

print(lts[0])
print(lts[-1])
print(lts[1:4])

del lts[-1]
lts.append('Python')
lts.remove('Python')
print(lts)
