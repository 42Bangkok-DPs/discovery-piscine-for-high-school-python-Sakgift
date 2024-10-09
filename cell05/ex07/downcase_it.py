import sys
num_param = [arg.lower() for arg in sys.argv[1:]]
if num_param:
    print(num_param)
else:
    print("none")