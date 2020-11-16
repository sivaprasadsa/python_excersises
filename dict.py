import os
direc= 'files/'
file_dic= {}

list_files= [i for i in os.listdir(direc)]
#list_time = [j for j in  os.path.getctime(direc)]
#print(list_files)
for key in file_dic: 
    for value in list_time: 
        file_dic[key] = value 
        break 
#print(list_time)
for i in list_files:
    key = list_files.index(i)+1
    file_dic[key]=i
print (file_dic)