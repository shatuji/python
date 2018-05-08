#dictionary
fruit = {'apple':12,'banana':10,'orange':7}
print(fruit)
fruit['egg'] = 3.6
print(fruit)
print('***'*23)
print(fruit['apple'])
print(list(fruit.keys()))
print(sorted(fruit.keys()))
print('--'*12)
print({x:x**6 for x in range(34) if x <= 30})
