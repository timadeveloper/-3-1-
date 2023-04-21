l = [1, 4, 1, 6, "hello", 5, "hello"]
print(l)
l_unique = []
for i in l:
	if i not in l_unique:
		l_unique.append(i)
print(l_unique)