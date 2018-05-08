#zip lambda map
a = [1,324,32]
b = [12,34,2]
obj = zip(a,b)
#print(list(obj))

#for u in list(obj):
#s    print(u)

#for i , j in obj:
#    print(i*2,j*3)


def function1(x , y):
    return x+y

#this is just liking invoked function that get it return data 
result_map = map(function1,[2,32],[3,23])
print(list(result_map))
