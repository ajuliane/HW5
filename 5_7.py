import json
i=1
profit=0
average=0
number=0
big_list=list()
dict1=dict()
dict2=dict()
a=str()
with open('7.txt', 'r') as f:

    lines = f.readlines()
    for line in lines:
        list=line.split()
        profit=float(list[2])-float(list[3])
        if profit > 0:
            print(f'Profit {i} company: {profit}')
            average=average+profit
            number=number+1
        a=str(list[0])
        dict1[a]=profit
        i=i+1
    print(f'Average profit is: {average/number}')
    dict2['average profit']=average/number
    big_list.append(dict1)
    big_list.append(dict2)
    # print(dict1)
    # print(dict2)

# b = {'salary': 50000, 'bonus': [10000, 1000]}
# data = {'income': b}
with open('7_result.json', 'w') as f:
     json.dump(big_list, f)