sum=0
with open('5', 'w+') as f:
    f.write('345 4567 5678 5678')
    f.seek(0)
    line = f.readline()
    #print(line)
    numbers = line.split()
    #print(numbers)
    for i in numbers:
        sum = sum + int(i)
    print(sum)
