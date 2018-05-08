#loop techniques
phone = {'apple':8880,'xiaomi':1230,'honor':'12066'}

for k,v in phone.items():
    print('keys:',k,',value:',v)


for d,v in phone.items():
    print(d , v)

lists_collection = ('1','23','55')
print(lists_collection)
for i , v in enumerate(lists_collection):
    print(i , v)

question = ['name' , 'quest' , 'favorite color']
answers = ['lancelot' , 'the holy grail' , 'blue']
for q,a in zip(question , answers):
    print('what is your {0}? it is {1}'.format(a,q))

for i in reversed(range(0,100,3)):
    if i >1 :
        print(i)


pen = ['pensil','pen','water-pen']
for i in sorted(pen):
    print(i)
