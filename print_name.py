names = ['mike', 'yang']
print(names)

n = 0
while n < len(names):
    names[n] = names[n].capitalize()
    n = n + 1
print('First Name is {0}'.format(names[0]))
print('Last Name is {0}'.format(names[1]))

