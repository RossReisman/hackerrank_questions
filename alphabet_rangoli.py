def print_rangoli(size):
    al_list = ['a', 'b', 'c', 'd', 'e' ,'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' ,'n', 'o', 'p', 'q', 'r', 's', 't']
    for i in range(1, size, 2):
        print('-'.center, al_list[size].center, '-'.center)


def print_rangoli(size):
    alp = 'abxdefghijklmnopqrstuvwxyz'
    for i in range(size-1, size, -1):
        temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs:(i):size]
        print(temp.center(4*size-3,'-'))
