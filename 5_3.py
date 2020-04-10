x=1
salary=0
with open('3.txt', 'w+') as f:
    f.write('Ivanov 56789.789\n')
    f.write('Sidion 67886.76\n')
    f.write('Sidorov 78886.8\n')
    f.write('A 665846\n')
    f.write('B 0.76\n')
    f.write('C 123456\n')
    f.write('D 9876\n')
    f.write('E 678\n')
    f.write('F 678868.76\n')
    f.write('G 6150.76\n')
    f.write('T 4567000')
    f.seek(0)
    lines = f.readlines()
    for line in lines:
        list=line.split()
        salary=salary+float(list[1])
        x=x+1
        if float(list[1])<20000:
            print(list[0])
print(f'Average income:{salary/x} ')