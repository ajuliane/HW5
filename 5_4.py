f2 = open('4_1.txt', 'w')
with open('4', 'r') as f:
    lines = f.readlines()
    print(f'The file contains:{len(lines)} lines')
    # print(lines)
    for line in lines:
        list = line.split()
        # print(list)
        if list[0] == 'One':
            list[0] = 'Один'
        if list[0] == 'Two':
            list[0] = 'Два'
        if list[0] == 'Three':
            list[0] = 'Три'
        if list[0] == 'Four':
            list[0] = 'Четыре'
        if len(list) > 1:
            f2.write(f'{list[0]+list[1]+list[2]}\n')
f2.close()
