i=1
with open('2', 'w+') as f:
    f.write('vndkjv mkdfk vdmddl v do\n')
    f.write('vdf jnfd fjij jid\n')
    f.write('zxc')
    f.seek(0)
    lines = f.readlines()
    print(f'The file contains:{len(lines)} lines')
    # print(lines)
    for line in lines:
        print(f'The line {i} contains: {len(line.split())} words')
        i=i+1

