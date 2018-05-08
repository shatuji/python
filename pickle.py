#pickle
import pickle
a_dict = {'asd':'hh',6:'huh',3:{'asff':'u',43:8},'l':[23,4,2,123]}
##file = open('pickle_file.pickle','wb') #open method that write binary
##pickle.dump(a_dict,file)
##file.close()

#file = open('pickle_file.pickle','rb') # this is meaning read binary from pickle file
#new_dic = pickle.load(file)
#file.close()
#print(new_dic)

#then you can use with keyword to open file
#if you use this keyword that auto close file
with open('pickle_file.pickle','rb') as f:
    print(pickle.load(f))
