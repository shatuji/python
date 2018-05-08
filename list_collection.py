#list collection
color = ['red','white','green','yellow','gray','white','pink','black','red']
print(len(color))
print('--'*29)
varible = color.count('red')
varible = color.count('goden')
print(varible)
print('--'*29)
#index()
print(color.index('white'))
print(color.index('red',3))

#reverse()
color.reverse()
print(color)

#sort()
color.sort(reverse = True)
print(color)

#pop()
color.pop(0)
print(color)

#append()
color.append('yellow')
print(color)

#insert()
color.insert(0,'blue')
print(color)

#remove() Remove the first item from the list whose value is x, It is error if there is no such item
#color.remove('red')
print(color)
print('--'*29)

#copy()

print(color.copy())

