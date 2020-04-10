with open('1.txt', 'w') as f:
    text = input('Please enter something: ')
    list=text.split()
    f.write('\n'.join(text))