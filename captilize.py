def solve(s):
    l = s.split(" ")
    str = ""
    for i in range(len(l)):
        str += l[i].capitalize() + " "
    return str
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
