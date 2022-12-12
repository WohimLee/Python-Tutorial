import pickle, pprint 

# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}

# data2 = [1, 2, 3, 4]
# data2.append(data2)
        
# with open('./files/test.pkl', 'wb') as f:
#     pickle.dump(data1, f)
#     pickle.dump(data2, f, -1)

with open("./files/test.pkl", 'rb') as f:
    data1 = pickle.load(f)
    pprint.pprint(data1)
    # print(data1)

    data2 = pickle.load(f)
    pprint.pprint(data2)
    # print(data2)




