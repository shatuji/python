#tuple and sequences
t = 1,8,'t','t'
print(t)

#sets 
basket = {'apple','orange','pear','apple','orange'}
print(basket)

print('pear' in basket)
print('pears' in basket)

a = set('asfhkasdhfaksf')
b = set('asfh')

print('this is a value:',a)
print('this is b value:',b)
print('this is a-b value:',a-b)
# error unsupported operand type(s) for +:'set' and 'set'
#print('this is a+b value:',a+b) 
print('this is a|b value:',a|b)
print('this is a&b value:',a&b)
print('this is a^b value:',a^b)

#similarly to list comprehension ,set comprehension are alse supported:
d = {x**3 for x in range(4) if x < 2}
print('this is d value and less then 100:',d)
