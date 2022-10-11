import random

ls = ['plov', 'manty', 'kuurdak', 'lagman', 'oromo']
p = 0
m = 0
k = 0
l = 0
o = 0
for x in range(0, 100001):
    # print(x)
    choice = random.choice(ls)
    print(choice) 
    if choice == 'plov':
        p +=1
        print('plov')
    elif choice == 'manty':
        m += 1
        print('manty')
    elif choice == 'kuurdak':
        k += 1
        print('kuurdak')
    elif choice == 'lagman':
        l += 1
        print('lagman')
    else:
        o += 1
        print('oromo')

print('результаты голодных игр: ')
print(f'plov: {p}\nmanty: {m}\nkuurdak: {k}\nlagman: {l}\noromo: {o}')


































