file = open('my file.txt','r')
content = file.readline()
print(content)
second_content = file.readline()
print(second_content)

all_content = file.readlines()
print(all_content)
