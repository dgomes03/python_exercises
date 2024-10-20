import sys

try:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        if sys.argv[1].endswith('.py'):
            with open(sys.argv[1],"r") as lines:
                N=0
                for line in lines:
                    if line.lstrip().startswith("#"):
                        N+=0
                    elif line.strip() == "":
                        N+=0
                    else:
                        N+=1
            print(N)
        else:
            print("Not a Python file")
            sys.exit(1)
except(FileNotFoundError):
        sys.exit("File does not exist")
