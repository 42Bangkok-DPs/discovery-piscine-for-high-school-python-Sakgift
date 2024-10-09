import sys
A = sys.argv[1:]
if len(A) < 2:
        print("none")
else:
    for B in reversed(A):
        print(B)