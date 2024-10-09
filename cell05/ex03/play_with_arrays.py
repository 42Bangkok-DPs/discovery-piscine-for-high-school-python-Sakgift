A = [2, 8, 9, 48, 8, 22, -12, 2]
B = [x + 2 for x in A if x > 5]
c = list(set(B))
print(A)
print(c)