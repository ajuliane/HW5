my_dict=dict()
s=0
with open('6.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:

        #list=' '.join(line.split())
        my_list=line.split()
        print(my_list)
        for id,value in enumerate(my_list):
            if id == 0:
                a=value
            else:
                s=s+int(value.split('(')[0])
            my_dict[a]=s
        s = 0
print(my_dict)
