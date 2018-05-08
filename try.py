#TRY TUTORIAL
try:
    file = open('new fileS' , 'r')
except Exception as es:
    print('this is no file named as new file')
    response = input('please input data')
    if response == 'y':
        file = open('new file','w')
    else:
        pass
#else:
#    file.write('this is good test for us')
#    file.close()
