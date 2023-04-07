def print_formatted(number):
    # your code goes here
 
    l=len(bin(number)[2::])
    
    for c in range(1,number+1):
        octa=oct(c)
        hexa=hex(c).upper()
        bina=bin(c)
        print(str(c).rjust(l),str(octa[2::]).rjust(l),str(hexa [2::]).rjust(l),str(bina[2::]).rjust(l))
    
    return 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
